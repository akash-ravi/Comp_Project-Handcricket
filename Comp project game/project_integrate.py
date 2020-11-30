import mysql.connector , os , time                  # import everything
from colorama import Fore , Style , Back
from tabulate import tabulate


login_status='logged_out'                           #global variables
uname=''
table_name=''

def clear():                                 #clear terminal
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def checkalnum(st):                                                 #Password alphanumeric check
    alpha=0
    digit=0
    for i in range (0,len(st)):
        if st[i].isalpha()==True:
            alpha=1
        elif st[i].isdigit()==True:
            digit=1
    if alpha==1 and digit==1:
        return True
    else:
        return False        

conn=mysql.connector.connect(user='root', password='root123', host='localhost')
m=conn.cursor()

try: 
    create_db="create database python"
    m.execute(create_db)
    conn.commit()
except:
    pass
use_db="use python"
m.execute(use_db)
conn.commit()
try:
    create_login_table="create table LOGIN(username varchar(20) NOT NULL PRIMARY KEY,password varchar(20), login_status varchar(20) DEFAULT 'logged_out', coins int DEFAULT 800, new_user int default 0)"
    m.execute(create_login_table)
    conn.commit()
except:
    pass

try:
    create_table_list="CREATE TABLE PLAYER_LIST_FOR_AUCTION(No INT AUTO_INCREMENT PRIMARY KEY ,PLAYER_NAME VARCHAR(40), PLAYER_SALARY VARCHAR(5))"
    m.execute(create_table_list)
    conn.commit()
    with open(r'static/Players_list.txt','r') as file:
        x=file.readlines()
    for i in range(0,len(x),2):
        x[i]=x[i][0:-1]
        x[i+1]=x[i+1][0:-1]
        add_player="insert into PLAYER_LIST_FOR_AUCTION(PLAYER_NAME , PLAYER_SALARY) values( '{}','{}')".format(x[i],x[i+1])
        m.execute(add_player)
        conn.commit()
except:
    pass

def login():
    global login_status , uname , table_name
    admin_create="insert into LOGIN (username,password) values('{}', '{}')".format("admin123","root123")
    try:
        m.execute(admin_create)
        conn.commit()
    except:
        pass

    #ucount=0
    clear()
    while True:
        try:
            print(Fore.CYAN+"WELCOME!\nWhat would you like to do?\n1. Create Account\n2. Login\n3. Change password\n4. Kill program"+Style.RESET_ALL)
            l1=int(input(Fore.BLUE+"Please select an option using the numbers corresponding to the option:\n"+Style.RESET_ALL))
            clear()
        except:
            #print("Invalid option")
            print(Fore.RED + 'Invalid option provided!' + Style.RESET_ALL)
            continue
        if l1 in [1,2,3,4]:
            if l1==1:
                while True: 
                    print(Fore.GREEN+"Please enter an alphanumeric password"+Style.RESET_ALL)
                    uname=input(Fore.BLUE+"Enter username: "+Style.RESET_ALL)
                    try:
                        adduname="insert into LOGIN(username) values('{}')".format(uname)
                        m.execute(adduname)
                        pass
                    except:
                        print(Fore.RED+"Username already exists, please enter another username"+Style.RESET_ALL)
                        time.sleep(3)
                        continue
                    while True:
                        pwd=input(Fore.BLUE+"Enter password: "+Style.RESET_ALL)
                        if checkalnum(pwd)==True:
                            add="update LOGIN set password='{}' where username='{}'".format(pwd, uname)
                            m.execute(add)
                            conn.commit()
                            print(Fore.GREEN+"Account created successfully"+Style.RESET_ALL)
                            time.sleep(3)
                            clear()
                            break
                        else:
                            print(Fore.RED+"Password must contain letters as well as numbers"+Style.RESET_ALL)
                            time.sleep(3)
                            clear()
                            print(Fore.BLUE+"Enter username: "+Style.RESET_ALL+uname)
                            continue
                    break
                table_name=uname + '_matches_history'
                st="create table {}(Game_No INT AUTO_INCREMENT PRIMARY KEY , YOUR_BATTING varchar(20), YOUR_BOWLING varchar(20), RESULT varchar(100))".format(table_name)
                m.execute(st)
                conn.commit()
                
                continue
            elif l1==2:
                while True:
                    uname=input(Fore.BLUE+"Enter username: "+Style.RESET_ALL)
                    checkpass="select * from LOGIN where username='{}'".format(uname)
                    log1=m.execute(checkpass)
                    y=m.fetchall()
                    if len(y)==0:
                        #print("Invalid username")
                        print(Fore.RED + 'Invalid option provided!' + Style.RESET_ALL)
                        time.sleep(3)
                        clear()
                        continue
                    else:
                        while True:
                            pwd=input(Fore.BLUE+"Enter password: "+Style.RESET_ALL)
                            for i in y:
                                if  i[1]==pwd:
                                    print(Fore.GREEN+"Welcome,",uname+Style.RESET_ALL)
                                    temp=True
                                    time.sleep(3)
                                    clear()
                                    break
                                elif i[1]!=pwd:
                                    #print("Incorrect password")
                                    print(Fore.RED + 'Incorrect password!' + Style.RESET_ALL)
                                    temp=False
                                    time.sleep(3)
                                    clear()
                                    print(Fore.BLUE+"Enter username: "+Style.RESET_ALL,uname)
                                    break
                            if temp==True:
                                break
                            elif temp==False:
                                continue
                        break
                    
                    break
                login_status='logged_in'
                changestatus="update LOGIN set login_status='{}' where username='{}'"
                m.execute(changestatus.format(login_status,uname))
                conn.commit()
                table_name=uname + '_matches_history'
                table_exist_checker="SELECT * FROM {}".format(table_name)
                m.execute(table_exist_checker)
                result=m.fetchall()
                if result==None:
                    pass
                
                fetch_user_status="select new_user from LOGIN where username='{}'".format(uname)
                m.execute(fetch_user_status)
                z=m.fetchone()
                if z[0]==0:
                    '''try:
                        create_squad="create table SQUAD_"+uname+"(Sl_No int auto_increment primary key, Playername varchar(40))"
                        m.execute(create_squad) 
                        conn.commit()
                    except:
                        pass'''
                    while True:
                        print(Fore.CYAN+"You have 800 coins ")
                        print('Please select your team')
                        print('Players in the game to buy'+Style.RESET_ALL)
                        headers_players=['No ','PLAYER_NAME','PLAYER_SALARY']
                        m.execute("select * from PLAYER_LIST_FOR_AUCTION order by No")
                        player_names=m.fetchall()
                        print(tabulate(player_names, headers_players, tablefmt="psql"))
                        print(Fore.CYAN+'Please select 11 players'+Style.RESET_ALL)
                        player_list=[]
                        players_names=[]
                        cost=0
                        error=0
                        for i in range(1,12):
                            try:
                                while True:
                                    print(Fore.BLUE+'Enter the Serial Number of the player you want to select \nplayer',i,' : ',end=''+Style.RESET_ALL)
                                    player_name=int(input(''))
                                    if player_name in players_names:
                                        print(Fore.RED + 'Player not available\nPlease select a player that has not been selected before' + Style.RESET_ALL)
                                        continue
                                    players_names.append(player_name)
                                    if player_name in range(1,len(player_names)+1):
                                        break
                                    else :
                                        print(Fore.RED + 'Player not available\nPlease select a number within the given range of numbers'  + Style.RESET_ALL)
                                        continue
                            except:
                                print(Fore.RED + 'Invalid option provided!' + Style.RESET_ALL)
                            playername_buy="SELECT PLAYER_NAME FROM PLAYER_LIST_FOR_AUCTION where No={} ".format(player_name)
                            m.execute(playername_buy)
                            playername_bought=m.fetchall()
                            playername_bought=playername_bought[0][0]
                            playersalary_buy="SELECT PLAYER_SALARY FROM PLAYER_LIST_FOR_AUCTION where No={} ".format(player_name)
                            m.execute(playersalary_buy)
                            playersalary_bought=m.fetchall()
                            playersalary_bought=int(str(playersalary_bought[0][0]))
                            player_list.append(playername_bought)
                            cost+=playersalary_bought
                            if cost>800:
                                error=1
                                print()
                                print(Fore.RED + 'Your team is too op team cant be paid more than 800 coins \nsorry\nresetting selection process\n'  + Style.RESET_ALL)
                                time.sleep(5)
                                clear()
                                break
                        if error==1:
                            continue
                        else :
                            pass
                        teamtable="create table MYSQUAD_"+uname+"(No int AUTO_INCREMENT PRIMARY KEY , PlayerName varchar(40) UNIQUE KEY)"
                        m.execute(teamtable)
                        conn.commit()
                        for i in range(len(player_list)):
                            addplayer1="insert into MYSQUAD_"+uname+"(PlayerName) values ('{}')".format(player_list[i])
                            m.execute(addplayer1)
                            conn.commit()
                        coin_adjust="update LOGIN set coins=coins-{} where username='{}'".format(cost,uname)
                        m.execute(coin_adjust)
                        conn.commit()
                        m.execute("select * from MYSQUAD_"+uname+" order by No ")
                        my_squad=m.fetchall()
                        print()
                        print(Fore.GREEN+uname,"'s squad is : "+Style.RESET_ALL)
                        print(tabulate(my_squad, tablefmt="psql"))
                        print()
                        getcash="select coins from LOGIN where username='{}'".format(uname)
                        m.execute(getcash)
                        coins=m.fetchone()
                        print(Fore.CYAN+'Coins remaining is',coins[0],'coins'+Style.RESET_ALL)
                        break
                    update_new_user="update LOGIN set new_user=1 where username='{}'".format(uname)   
                    m.execute(update_new_user)   
                    conn.commit()
                    time.sleep(10)   
                elif z[0]==1:
                    pass
                break
            
            elif l1==3:
                uname=input(Fore.BLUE+"Enter username: "+Style.RESET_ALL)
                findpass="select * from LOGIN where username='{}'".format(uname)
                log2=m.execute(findpass)
                y=m.fetchall()
                if len(y)==0:
                    #print("Invalid username")
                    print(Fore.RED + 'Invalid username!' + Style.RESET_ALL)
                    time.sleep(3)
                    clear()
                    continue
                else: 
                    while True:
                        pwd=input(Fore.BLUE+"Enter old password: "+Style.RESET_ALL)
                        for i in y:
                            if pwd in i:
                                newpass=input(Fore.BLUE+"Enter new password: "+Style.RESET_ALL)
                                if checkalnum(newpass)==True:
                                    changepass="update LOGIN set password='{}' where username='{}'"
                                    m.execute(changepass.format(newpass,uname))
                                    conn.commit()
                                    print(Fore.GREEN+"Your password has been succesfully updated"+Style.RESET_ALL)
                                    temp=True
                                    time.sleep(3)
                                    clear()
                                    break
                                else: 
                                    print(Fore.RED+"Password must contain both letters and numbers"+Style.RESET_ALL)
                                    temp=False
                                    time.sleep(5)
                                    clear()
                                    break
                            elif pwd not in i:
                                #print("Invalid/incorrect password, please enter the most recent password")
                                print(Fore.RED + 'Invalid/incorrect password, please enter the most recent password!' + Style.RESET_ALL)
                                temp=False
                                time.sleep(3)
                                clear()
                                break
                        if temp==True:
                            break
                        elif temp==False:
                            continue
            elif l1==4:
                print(Fore.RED+'program terminated'+Style.RESET_ALL)
                if login_status=='logged_in':
                    login_status='logged_out'
                    changestatus="update LOGIN set login_status='{}' where username='{}'"
                    m.execute(changestatus.format(login_status,uname))
                    conn.commit()
                    print(login_status,uname)
        
        else: 
            #print("Invalid option")
            print(Fore.RED + 'Invalid option provided!' + Style.RESET_ALL)
            time.sleep(3)
            clear()
            continue
        break
    time.sleep(5)
    clear()


def store(): 
    global uname
    getplayers="select PLAYER_NAME from PLAYER_LIST_FOR_AUCTION"
    m.execute(getplayers)
    p1=m.fetchall()
    getsquad="select PlayerName from MYSQUAD_"+uname
    m.execute(getsquad)
    p2=m.fetchall()
    p3=p1[::]
    for i in p1:
        if i in p2:
            p3.remove(i)
        elif i not in p2:
            continue
    to_buy=[]
    for i in p3:
        getpurchaselist="select * from PLAYER_LIST_FOR_AUCTION where PLAYER_NAME='{}'".format(i[0])
        m.execute(getpurchaselist)
        z=m.fetchall()
        to_buy.append(z[0])
    print()
    print(Fore.CYAN+"Here is the list of players you can buy : "+Style.RESET_ALL)
    to_buy_select=[]
    for i in range(len(to_buy)):
        a=list(to_buy[i])
        a[0]=i+1
        to_buy_select.append(a)
    print(tabulate(to_buy_select,headers=["No","Player Name","Price"], tablefmt="psql"))
    print()

    while True:
        checkcoin="select coins from LOGIN where username='{}'".format(uname)
        m.execute(checkcoin)
        coinval=m.fetchone()
        coinval=coinval[0]
        print(Fore.CYAN+"You have ",coinval,"coins remaining "+Style.RESET_ALL)
        try:
            buyno=int(input(Fore.BLUE+"Enter No of the player you want to purchase : "+Style.RESET_ALL))
            if buyno in range(1,len(to_buy_select)+1):
                pass
            else :
                print(Fore.RED + 'Invalid option provided!\nPlayer either doesnt exist in game or you already have him' + Style.RESET_ALL)
                continue
        except:
            print(Fore.RED + 'Invalid option provided!' + Style.RESET_ALL)
            continue

        buyval=buyno-1
        
        
        if coinval>=int(to_buy_select[buyval][2]):
            addplayer="insert into mysquad_"+uname+"(PlayerName) values('{}')".format(to_buy_select[buyval][1])
            m.execute(addplayer)
            conn.commit()
            cutprice="update LOGIN set coins=coins-"+to_buy_select[buyval][2]+" where username='{}'".format(uname)
            m.execute(cutprice)
            conn.commit()
            getremaining="select coins from LOGIN where username='{}'".format(uname)
            m.execute(getremaining)
            leftover=m.fetchone()
            print()
            print(Fore.GREEN+"Purchase successful!\nYou have",leftover[0],"coins remaining"+Style.RESET_ALL)
            to_buy_select.pop(buyval)
            pass
        elif coinval<=int(to_buy_select[buyval][2]):
            print(Fore.RED+"Not enough coins, please come again later after playing more games!"+Style.RESET_ALL)
            continue

        buymore=input(Fore.BLUE+"Would you like to buy more players?\nPress y for yes and n for no: "+Style.RESET_ALL)
        if buymore=="y" or buymore=="Y":
            for i in range(len(to_buy_select)):
                to_buy_select[i][0]=i+1
            print(tabulate(to_buy_select,headers=["No","Player Name","Price"], tablefmt="psql"))
            continue
        elif buymore=="n" or buymore=="N":
            break
        else :
            print(Fore.RED + 'Invalid option provided!' + Style.RESET_ALL)
            continue

login()
#login_status='logged_in'
#clear()


if login_status=='logged_in':
    while True:
        print('----------------------------LOGGED IN AS {}----------------------------'.format(uname))
        time.sleep(2)
        print(Fore.CYAN+'Please select what you want to do:\n1. Play a game\n2. View Players Store\n3. View summary of game history'+Style.RESET_ALL)
        try:
            gg=int(input(''))
            if gg in range(1,4):
                break
            else:
                print(Fore.RED + 'Invalid option provided!' + Style.RESET_ALL)
                time.sleep(3)
                clear()
                continue
        except:
            print(Fore.RED + 'Invalid datatype provided!' + Style.RESET_ALL)
    if gg==1:
        exec(open('game_logic.py').read())
        #import game_logic
    elif gg==2:
        store()
    elif gg==3:
        print(table_name)
        st="SELECT * from {} order by Game_No".format(table_name)
        m.execute(st)
        history_of_scores=m.fetchall()
        headers=["Game_No","YOUR_BATTING","YOUR_BOWLING","RESULT"]
        print(tabulate(history_of_scores, headers, tablefmt="psql"))
        conn.commit()
        time.sleep(10)
        clear()
        
    while True:
        ggg=str(input(Fore.BLUE+'What do you want to do\n1. Play another game\n2. View Players Store\n3. View summary of game history\n4. Logout\n'+Style.RESET_ALL))
        ggg.strip()
        if ggg=='1':
            exec(open('game_logic.py').read())
            '''if gg!=1:
                import game_logic
            else :
                pass # here how to run game logic
                print('sorry we are working on it')'''
        elif ggg=='2':
            store()                     #open player store code
        elif ggg=='3':
            st="SELECT * from {} order by Game_No".format(table_name)
            m.execute(st)
            history_of_scores=m.fetchall()
            headers=["Game_No","YOUR_BATTING","YOUR_BOWLING","RESULT"]
            print(tabulate(history_of_scores, headers, tablefmt="psql"))
            conn.commit()
            time.sleep(10)
            clear()
        elif ggg=='4':
            login_status='logged_out'
            changestatus="update LOGIN set login_status='{}' where username='{}'"
            m.execute(changestatus.format(login_status,uname))
            conn.commit()
            print('logging out of account',uname)
            print('thank you for playing this game')
            break
        else:
            print(Fore.RED + 'Invalid option provided!' + Style.RESET_ALL)
            print(Fore.BLUE+"Enter option from 1 to 4"+Style.RESET_ALL)
            continue
conn.close()
