# Script that deals with manipulating the data
for n in range(1,71):
    if n >= 10:
        in_num = str(n)
    else:
        in_num = '0'+str(n);
    print in_num
    in_file = open('/Diabetes-Data/data-' + in_num, 'r')

    for line in in_file:

        # Break up string by spaces
        word_list = line.split()
        if len(word_list)!=4:
            continue
        
        date_list = word_list[0].split('-')
        mn = date_list[0]
        dy = date_list[1]
        yr = date_list[2]
        time_list = word_list[1].split(':')
        tm = int(time_list[0])*60+int(time_list[1])
        code = word_list[2]
        val = word_list[3]
        #print str(val)+' '+str(code)
        fnam = 'data-fromated-'+str(code)+'.csv'
        out_file = open('/Diabetes-Output/'+fnam, 'a')
        s = str(mn)+','+str(dy)+','+str(yr)+','+str(tm)+','+str(val)
        out_file.write(s + '\n')
        out_file.close()    

    in_file.close()
    
