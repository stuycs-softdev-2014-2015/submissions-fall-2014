// When the user clicks on the "FIND OUT" button...
document.getElementById("start-button").onclick = function() {
    // Ask for permission to read the mailbox
    FB.login(getUserData, {scope: 'read_mailbox'});
}

// These are global variables.
// Before the user chooses a friend, this contains 50 most recent threads
var all_threads;

// Of type Thread, defined by FB at https://developers.facebook.com/docs/graph-api/reference/v2.2/thread
var thread;

// Basic data like name, gender, locale.
// Called in getUserData() through "/me"
var user_data;

// Nice to have
var friend_name = "";
var friend_first_name;

// Array of objects. Important properties: `created_time`, `from`, `message`
var messages = [];
var messagesFromOther=[];
var messagesFromYou=[];

// The messages used to entertain the user while we fetch messages & compute stuff.
// We save the timer so that we can cancel it when the computation is finished.
var loading_messages_timer;
var loading_messages = ["Crunching Numbers...", "Contacting Friends...", "Reading Diaries...", "Analyzing Facial Expressions..."];

var MAX_MESSAGES_TO_LOAD = 400;

// Get the user's name, locale, etc.
// This is the callback from the login button onclic
function getUserData() {
    FB.api("/me", getInbox);
}

// Get all messages in inbox
// This is the callback from getUserData()
function getInbox(response) {
    if (response.error) {
        handleError(response.error);
        return;
    }

    user_data = response;

    // Get 50 most recent threads. 50 is the max.
    FB.api("/me/inbox", {limit: 50 }, displayFriends);
}

// List friends, and let the user choose the friend he/she likes.
// This is the callback from getInbox()
function displayFriends(response) {
    if (response.error) {
        handleError(response.error);
        return;
    }

    // Hide start button, display instructions
    prepareFriendList();

    // all_threads = the 50 most recent chat threads
    all_threads = response.data;

    // for each, add to the friend list
    all_threads.forEach(function(thread, thread_index) {
        // only if it's a one-on-one conversation
        if (thread.to.data.length == 2)
        addToFriendsList(thread_index);
    } );

    // Set click listeners on the list
    listenForClicks();
}

// Hide start button, display instructions
// Called by displayFriends()
function prepareFriendList() {
    // Vanilla JS, sorry
    document.getElementById("start-button").style.display = "none";
    var all_friends_element = document.querySelector("#friendList ul");
    var instructions_element = document.createElement("h2");
    var instructions_text_element = document.createTextNode("WHO IS IT?");

    instructions_element.appendChild(instructions_text_element);
    all_friends_element.appendChild(instructions_element);
}

// Add the person's name from the given thread to the list
// Called by displayFriends()
function addToFriendsList(thread_index) {
    var thread = all_threads[thread_index];
    var participants = thread.to.data;
    var other_person_index = participants[0].name == user_data.name ? 1 : 0;
    var other_person = participants[other_person_index];

    // Vanilla JS, sorry
    var all_friends_element = document.querySelector("#friendList ul");

    var friend_list_element = document.createElement("li");
    friend_list_element.setAttribute("data-name", other_person.name);
    friend_list_element.setAttribute("data-thread-index", thread_index);

    var friend_link_element = document.createElement("a");
    friend_link_element.href = "#";

    var friend_name_element = document.createElement("p");
    friend_name_element.className = "friendName"

    var friend_text_element = document.createTextNode(other_person.name);
    var friend_image_element = document.createElement("img");
    friend_image_element.src = "https://graph.facebook.com/" + other_person.id + "/picture?height=100&height=100";

    friend_link_element.appendChild(friend_image_element);
    friend_name_element.appendChild(friend_text_element);
    friend_link_element.appendChild(friend_name_element);
    friend_list_element.appendChild(friend_link_element);
    all_friends_element.appendChild(friend_list_element);
}

// Set click listeners
// Called by displayFriends()
function listenForClicks() {
    var all_links = document.querySelectorAll("#friendList li");

    // For every list item, specify what happens when user clicks on it
    for (var i = 0; i < all_links.length; i++) {
        var elem = all_links[i];
        elem.onclick = function() {
            friend_name = this.getAttribute("data-name");
            friend_first_name = getFriendFirstName();
            var thread_index = this.getAttribute("data-thread-index");
            // "Crunching numbers", etc
            showLoadingScreen();

            // We only get 25 messages per thread. We need to load more.
            loadAllMessages(thread_index);
            analyzeMessages();
        }
    }
}

function getFriendFirstName() {
    friend_first_name = friend_name.split(" ")[0];
}

function showLoadingScreen() {
    // Hide the friend list
    document.getElementById("friendList").style.display = "none";

    // From http://tobiasahlin.com/spinkit/
    var loadingScreenHTML = "\
                             <p id='loading' data-message-index='0'>Crunching Numbers...</p>\
                             <div class='spinner'>\
                             <div class='rect1'></div>\
                             <div class='rect2'></div>\
                             <div class='rect3'></div>\
                             <div class='rect4'></div>\
                             <div class='rect5'></div>\
                             </div>\
                             </div>";
    document.getElementById("loading-screen").innerHTML = loadingScreenHTML;
    loading_messages_timer = window.setInterval(changeLoadingMessage, 2400);
}

// Called at a regular interval
function changeLoadingMessage() {
    var loading_message_element = document.getElementById("loading");
    var current_message_index = loading_message_element.getAttribute("data-message-index");

    // Without the parseInt() current_message_index is string.
    // 30 minutes of terrible debugging
    var new_message_index = (parseInt(current_message_index, 10) + 1) % loading_messages.length;
    loading_message_element.setAttribute("data-message-index", new_message_index);
    loading_message_element.textContent = loading_messages[new_message_index];
}

function loadAllMessages(thread_index) {
    thread = all_threads[thread_index];
    messages = thread.comments.data;
    loadPageOfMessages(thread.comments.paging.next);
}

// Messages are divided up into pages.
// Each page contains a reference to the next (older) page
function loadPageOfMessages(url) {
    if (url== "")
        return;

    if (messages.length + 25 > MAX_MESSAGES_TO_LOAD)
        return;

    // Response is in JSON format
    var response_object = JSON.parse(getURL(url));
    var page_of_messages = response_object.data;
    messages.push.apply(messages, page_of_messages);

    if (messages.length + 25 <= MAX_MESSAGES_TO_LOAD && response_object.paging)
        loadPageOfMessages(response_object.paging.next);
}


// Not used, but useful for testing
function displayLoadedMessages() {
    var ul = document.createElement("ul");
    var li, text;
    messages.forEach(function(message) {
        li = document.createElement("li");
        text = document.createTextNode(message.from.name + ": " + message.message);
        li.appendChild(text);
        ul.appendChild(li);
    } );
    document.querySelector("#content").appendChild(ul);
}

function handleError(error) {
    alert("ERROR: " + error.message);
}

function analyzeMessages() {
    convertDatesToEpoch();
    sortMessagesByDate();
    splitMessagesBySender();

    var messageRatioRating = analyzeMessageRatio();
    var messageDelayRating = analyzeMessageDelays();
    var messageContentRating = analyzeMessageContent();
    //var messageTimesRating = analyzeMessageTimes();

    processResults(messageRatioRating, messageDelayRating, messageContentRating);
}

// Print out time differences between messages
// Most are positive, but some are negative!
// This means it's not perfectly chronologically sorted.
function debugMessageOrder() {
    timeDifferences = [];
    for (var i = 0; i < messages.length - 1; i++) {
        timeDifferences.push(Date.parse(messages[i + 1].created_time) - Date.parse(messages[i].created_time));
    }
    console.log(timeDifferences);
}

// By default the `created_at` field of messages is in a special string format
// Makes it hard to compare
function convertDatesToEpoch() {
    messages = messages.map(function(message) { 
        message.created_time_epoch = Date.parse(message.created_time);
        return message;
    } );
}

function sortMessagesByDate() {
    messages.sort(function(a, b) { return a - b });
}

// Split `messages` into two arrays, `messagesFromYou` and `messagesFromOther`
function splitMessagesBySender(){
    messages.forEach(function(message) {
        if (message.from.name == friend_name){
            messagesFromOther.push(message);
        }
        else {
            messagesFromYou.push(message);
        }
    } );
}

// Called by analyzeMessages(), returns 1-5
// Looks at ratio of her messages to your messages
function analyzeMessageRatio() {
    var percentage = (messagesFromOther.length * 100) / messages.length;
    // (it's 6 if she sent all messages, but that's unlikely)
    var rating = Math.floor(percentage / 20) + 1;
    return rating;

}

// Called by analyzeMessages(), returns 1-5
function analyzeMessageDelays() {
    return 2;
}

// Called by analyzeMessages(), returns 1-5
// Abandoned for now due to time zone difficulties
// Looks at the time of day during which you sent each other messages
// The deeper into the night, the better
function analyzeMessageTimes() {
    // Defining 3 a.m. as the gold standard for nightly discussion
    distances_to_3 = [];
    messages.forEach(function(message) {
        var distance_to_3_before = 1;
        var distance_to_3_after = 1;
        var closest_distance_to_3;
    } );
    return 0;
}

// Called by analyzeMessages(), returns 1-5
function analyzeMessageContent() {
    // Those count a lot
    var strikingWords = ["I like you", "hot", ";)", ":p"];
    // A colon followed by two characters that are not alphabet letters or spaces
    var emoticonsRegex = /:[^\w\s]{1,2}/g;

    var total_word_count = 0;
    var striking_word_count = 0;
    var emoticon_count = 0;
    messagesFromOther.forEach(function(message) {
        total_word_count++;
        // Count striking words
        strikingWords.forEach(function(strikingWord) {
            var striking_word_index = message.message.indexOf(strikingWord);
            while (striking_word_index != -1) {
                striking_word_count++;
                striking_word_index = message.message.indexOf(strikingWord, striking_word_index);
            }
        } );
        
        var emoticon_match = emoticonsRegex.exec(message.message);
        while (emoticon_match != null) {
            emoticon_count++;
            emoticon_match = emoticonsRegex.exec(message.message);
        }
        // Reset the regex
        emoticonsRegex.lastIndex = 0;
    } );
    
    var important_word_count = emoticon_count + 5 * striking_word_count;
    var percentage = 100 % important_word_count / total_word_count;
    var highest_threshold = 10;
    var lowest_threshold = 1;
    if (percentage > highest_threshold)
        return 5;
    if (percentage <= lowest_threshold)
        return 1;

    // I hardcoded it, should generalize later
    else {
        if (percentage <= 4)
            return 2;
        if (percentage <= 7)
            return 3;
        if (percentage <= 10)
            return 4;
    }
}

// Not used after all, but might be useful later
function getNumberOfWords(messageArray) {
    var word_count = 0;
    messageArray.forEach(function(message) {
        var number_of_words = message.message.split(" ").length;
        word_count += number_of_words;
    } );
    return word_count;
}

// Take the results, get ready to display them
function processResults(messageRatioRating, messageDelayRating, messageContentRating) {
    var averageRating = (messageRatioRating, messageDelayRating, messageContentRating) / 3;
    console.log(averageRating);

    // The timeout that switches the humurous loading messages
    clearTimeout(loading_messages_timer);

    // Convert 1-5 rating to a message for the user
    var verdict = getVerdict(averageRating);
    console.log(verdict);

    // Clear out previous HTML
    clearContent();
    displayResults(verdict);
}

// Clear out previous HTML
function clearContent() {
    var contentElement = document.getElementById("changing-content");
    while (contentElement.hasChildNodes()) {
        contentElement.removeChild(contentElement.lastChild);
    }
}

// Map rating (1-5) to message for the user
function getVerdict(rating) {
    // Let's give hope to our users and use ceil() instead of floor()
    var rating = Math.ceil(rating);
    var verdicts = [
        "We're not entirely sure that " + friend_first_name + " is aware of your existence.",
        "Sorry, " + user_data.friend_name + ", things don't look so good. Hey, we'll buy you a beer.",
        "We're not entirely sure...you and " + friend_first_name + " are a little close to be friends and a little distant to be into each other. Take care.",
        "Things are looking good, " + user_data.friend_name + ". Go for it.",
        "You and " + friend_first_name + " are a match made in heaven!"];
    return verdicts[rating + 1];
}

function displayResults(verdict) {
    var contentElement = document.getElementById("changing-content");
    var verdictElement = document.createElement("h2");
    var verdictTextElement = document.createTextNode(verdict);

    verdictElement.appendChild(verdictTextElement);
    contentElement.appendChild(verdictElement);
}

// http://stackoverflow.com/a/4033310/805556
function getURL(url)
{
    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, false);
    xmlHttp.send(null);
    return xmlHttp.responseText;
}
