import unittest
import login
from pymongo import Connection


collectionName = "testdatabase"
dbname = "testdb"


class defaultTest(unittest.TestCase):
    """Class for default setUp and tearDown methods for testing"""
    def setUp(self, names=["1", "2", "3"], dbname="testdb"):
        self.dbname = dbname
        self.names = names
        self.conn = Connection()
        self.db = self.conn[dbname]
        self._createTestDatabase(names)

    def _createTestDatabase(self, names):
        """iter(names)
        creates collection testdatabase from the list of names"""
        for name in names:
            self.db.testdatabase.insert(self._jsonify(name, "password", False))

    def _jsonify(self, name, password, authenticated):
        """string name, string password, boolean authenticated

        returns a dictionary in the form of json
        to insert into a mongo collection"""
        user = {'name': name,
                'password': password,
                'authenticated': True}
        return user

    def tearDown(self):
        self.db.testdatabase.drop()


class testIsInDatabase(defaultTest):
    def test_not_in_database(self):
        self.assertEquals(login.isInDatabase("notInDatabaseName",
                                             self.dbname,
                                             "testdatabase"), False)

    def test_in_database(self):
        for name in self.names:
            self.assertEquals(login.isInDatabase(name,
                                                 self.dbname,
                                                 "testdatabase"), True)


class testAddUser(defaultTest):
    def test_name_already_in_database(self):
        """Should return false and not add it into the database"""
        login.addUser("testingname", "password", self.dbname, "testdatabase")
        self.assertEquals(login.addUser("testingname",
                                        "password",
                                        self.dbname,
                                        "testdatabase"), False)

    def test_add_name_success(self):
        """Should return True and add user into the database"""
        self.assertEquals(login.addUser("testingname4",
                                        "password2",
                                        self.dbname,
                                        "testdatabase"), True)
        self.assertEquals(login.isInDatabase("testingname4",
                                             self.dbname,
                                             "testdatabase",), True)


class testUpdateUser(defaultTest):
    def test_not_in_database(self):
        """should return False and not insert user into the database"""
        success = login.updateUser("nameNotInDatabase",
                                   True,
                                   self.dbname,
                                   collectionName)
        success = success and login.updateUser("nameNotInDatabase",
                                               False,
                                               self.dbname,
                                               collectionName)
        self.assertEquals(success, False)

    def test_update_in_database_authenticated(self):
        """test if changing every person to authenticated works"""
        people = self.db[collectionName]

        totalUsers = people.count()

        for user in people.find():
            login.updateUser(user['name'], True, self.dbname, collectionName)

        totalLoggedInUsers = people.find({'authenticated': True}).count()
        self.assertEquals(totalUsers == totalLoggedInUsers, True)

    def test_update_in_database_not_authenticated(self):
        """test if changing every person to not authenticated works"""
        people = self.db[collectionName]

        totalUsers = people.count()

        for user in people.find():
            login.updateUser(user['name'], False, self.dbname, collectionName)

        totalLoggedOutUsers = people.find({'authenticated': False}).count()
        self.assertEquals(totalUsers == totalLoggedOutUsers, True)

    def test_password_invalid(self):
        """should return False and not log the user in"""
        people = self.db[collectionName]

        for user in people.find():
            success = login.login(user['name'], "invalid password",
                                  self.dbname, collectionName)

            self.assertEquals(success, False)

    def test_password_valid(self):
        """should return True and log the user in"""
        people = self.db[collectionName]

        totalUsers = people.count()

        for user in people.find():
            success = login.login(user['name'], user['password'],
                                  self.dbname, collectionName)

            self.assertEquals(success, True)

        totalLoggedInUsers = people.find({'authenticated': True}).count()
        self.assertEquals(totalUsers == totalLoggedInUsers, True)

    def test_logout(self):
        """return True and log the user out"""
        people = self.db[collectionName]

        totalUsers = people.count()

        for user in people.find():
            success = login.logout(user['name'], self.dbname, collectionName)

            self.assertEquals(success, True)

        totalLoggedOutUsers = people.find({'authenticated': False}).count()
        self.assertEquals(totalUsers == totalLoggedOutUsers, True)


def main():
        suite = unittest.TestLoader().loadTestsFromTestCase(testIsInDatabase)
        unittest.TextTestRunner(verbosity=2).run(suite)
        suite = unittest.TestLoader().loadTestsFromTestCase(testAddUser)
        unittest.TextTestRunner(verbosity=2).run(suite)
        suite = unittest.TestLoader().loadTestsFromTestCase(testUpdateUser)
        unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    main()
