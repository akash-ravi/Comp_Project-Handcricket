import mysql.connector , random, os , time 
from colorama import Fore , Style , Back
from tabulate import tabulate

conn=mysql.connector.connect(user='root', password='root123', host='localhost', database='python')
m=conn.cursor()

login_status="select username from LOGIN where login_status='{}'"
status="logged_in"
m.execute(login_status.format(status))
returned_values=m.fetchall()
conn.commit()
uname=returned_values[0][0]

table_name=uname + '_matches_history'
def clear():                                 #clear terminal
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
        

def toss(captain):         
    global bat_bowl_choice
    clear()
    print()
    print(Fore.CYAN+'NOW ITS TIME FOR THE TOSS'+Style.RESET_ALL)
    print(Fore.GREEN+captain,"IS COMING TO THE MIDDLE OF THE PITCH TO CALL THE TOSS"+Style.RESET_ALL)
    print('')
    print(Fore.YELLOW+'LOADING ...'+Style.RESET_ALL)
    time.sleep(3)
    


    x=random.randint(0,1)                                  #to make toss random 
    if x==0:
        print(Fore.RED+"Opponent captain calls the toss"+Style.RESET_ALL)
        print(Fore.YELLOW+'LOADING ...'+Style.RESET_ALL)
        time.sleep(3)
        

        toss_call=random.randint(0,3)

        if toss_call==0:
            print(Fore.RED+'OPPONENT WON THE TOSS AND HAS ELECTED TO BAT FIRST'+Style.RESET_ALL)
            bat_bowl_choice=2
        if toss_call==1:
            print(Fore.RED+'OPPONENT WON THE TOSS AND HAS ELECTED TO BOWL FIRST'+Style.RESET_ALL)
            bat_bowl_choice=1
        if toss_call==2 or toss_call==3:
            print(Fore.GREEN+"YOU HAVE WON THE TOSS: "+Style.RESET_ALL)
            print(Fore.BLUE+'WHAT DO YOU CHOOSE BATTING OR BOWLING'+Style.RESET_ALL)
            while True:
                try:
                    bat_bowl_choice=int(input(Fore.BLUE+"Enter 1 to bat first and 2 to chase: "+Style.RESET_ALL))
                except:
                    print(Fore.RED+'Enter valid data type: '+Style.RESET_ALL)
                    continue
                if bat_bowl_choice in [1,2]:
                    break
                else :
                    print(Fore.RED+'ENTER VALID OPTION : ')
        
        
    if x==1:
        print(Fore.CYAN+"You have to call the toss, do you choose heads or tails"+Style.RESET_ALL)
        while True:
            toss_choice=str(input(""))
            if toss_choice in ['heads','tails']:
                break
            else :
                print(Fore.RED+'ENTER VALID OPTION : heads or tails'+Style.RESET_ALL)
            print(Fore.YELLOW+'LOADING ...'+Style.RESET_ALL)
            time.sleep(3)
            

        a=random.randint(0,1)

        if a==0:
            call='heads'
        if a==1:
            call='tails'
        
        if call==toss_choice:
            print(Fore.GREEN+"YOU HAVE WON THE TOSS: "+Style.RESET_ALL)
            print(Fore.BLUE+'WHAT DO YOU CHOOSE BATTING OR BOWLING'+Style.RESET_ALL)
            while True:
                try:
                    bat_bowl_choice=int(input(Fore.BLUE+"enter 1 to bat first and 2 to chase: "+Style.RESET_ALL))
                except:
                    print(Fore.RED+'Enter valid data type: '+Style.RESET_ALL)
                    continue
                if bat_bowl_choice in [1,2]:
                    break
                else :
                    print(Fore.RED+'ENTER VALID OPTION : '+Style.RESET_ALL)
        
        else:
            toss_call=random.randint(0,1)
            if toss_call==0:
                print(Fore.RED+'OPPONENT WON THE TOSS AND HAS ELECTED TO BAT FIRST'+Style.RESET_ALL)
                bat_bowl_choice=2
            if toss_call==1:
                print(Fore.RED+'OPPONENT WON THE TOSS AND HAS ELECTED TO BOWL FIRST'+Style.RESET_ALL)
                bat_bowl_choice=1                   #if bat_bowl_choice=1 the batting if bat_bowl_choice=2 then bowling
    print(Fore.YELLOW+'LOADING ...'+Style.RESET_ALL)
    time.sleep(3)
    

    clear()

bat_bowl_choice=0
target=0
win=0
runs_result_list_for_table=[]

my_team=[]
opponent_team=[]
captain=''

def team_selection():
    global captain , my_team , opponent_team
    print_squad="select * from mysquad_{} order by No ".format(uname)                # for my team
    m.execute(print_squad)
    team=m.fetchall()
    if len(team)==11:
        for i in range(0,11):
            my_team.append(team[i][1])
    else :
        print(Fore.BLUE+"Please select your team(playing 11) from your squad : ")
        print(Fore.CYAN+'Your squad is : '+Style.RESET_ALL)
        print(tabulate(team,headers=['player name'], tablefmt="psql"))
        print()
        print(Fore.CYAN+'The first 2 players you select will be your openers \n1.on-strike \n2.non-strike  '+Style.RESET_ALL)
        print()
        l1=[]
        for i in range(11):
            while True:
                try:
                    print(Fore.BLUE+'Please enter your the serial no in squad of your team member : ')
                    print(i+1,". "+Style.RESET_ALL,sep='',end='')
                    player=int(input(''))
                    if player in range(1,len(team)+1):
                        if player not in l1:
                            l1.append(player)
                            break
                        elif player in l1:
                            print(Fore.RED+"Player already selected.\nPlease select another player"+Style.RESET_ALL)
                            continue
                except:
                    print(Fore.RED+'invalid datatype'+Style.RESET_ALL)
                    continue
                else :
                    print(Fore.RED+'player index out of range \nenter player no from 1-11'+Style.RESET_ALL)
            my_team.append(team[player-1][1])
    print()
    print(Fore.GREEN+'YOUR team(playing 11) : '+Style.RESET_ALL)
    #print(my_team)
    for i in my_team:
        print(i)
    #print(tabulate(my_team,headers=['player name'], tablefmt="psql"))  
    print()
    print(Fore.BLUE+'PLEASE SELECT YOUR CAPTAIN '+Style.RESET_ALL)
    try:
        captain=str(input(Fore.BLUE+"ENTER YOUR CAPTAIN's NAME: "+Style.RESET_ALL))
    except:
        print(Fore.RED+"INVALID DATA TYPE ENTER PLAYER NAME"+Style.RESET_ALL)
    while True:
        if captain not in my_team:
            print((Fore.RED+'INVALID INPUT ENETRED CAPTAIN NOT IN TEAM, ENTER PLAYER IN TEAM TO BE CAPTAIN '+Style.RESET_ALL))
            try:
                captain=str(input(Fore.BLUE+"ENTER YOUR CAPTAIN's NAME: "+Style.RESET_ALL))
            except:
                print(Fore.RED+"INVALID DATA TYPE ENTER PLAYER NAME"+Style.RESET_ALL)
        else :
            break
    print()
    print(Fore.GREEN+'Updated playing 11 : '+Style.RESET_ALL)
    for i in my_team:
        print(Fore.GREEN+i,end='  '+Style.RESET_ALL)
        if i==captain:
            print(Fore.GREEN+'c')
        else:
            print()
    print()
    
    m.execute("select PLAYER_NAME from PLAYER_LIST_FOR_AUCTION")
    player_names=m.fetchall()
    for i in range(len(player_names)):
        player_names[i]=player_names[i][0]
    #count=0
    opponent_team=[]
    while True:
        x=random.randint(0,len(player_names)-1)
        if len(opponent_team)==11:
            break
        elif player_names[x] not in my_team and player_names[x] not in opponent_team:
            opponent_team.append(player_names[x])
            #print(player_names[x])
            #print(opponent_team)
            #print(len(opponent_team))
            continue
    print(Fore.CYAN+'Opponent_team is being generated '+Style.RESET_ALL)
    print()
    time.sleep(5)    
    print(Fore.CYAN+'Opponent team is : '+Style.RESET_ALL)
    for i in opponent_team:
        print(Fore.GREEN+i)
    print()

    time.sleep(10)
    for i in range(100):
        clear()
    #squad selection over  
    print()

def batting_first():
    global my_team , opponent_team , target                                             #so i can access runs of the over and ball in both functions
    runs_this_innings=0
    wickets=0
    out_batsmen=[]
    runs_scored_by_batsman1=0
    runs_scored_by_batsman2=0
    balls_faced_by_batsman1=0
    balls_faced_by_batsman2=0
    batsman1=my_team[0]
    batsman2=my_team[1]
    bowler=''
    onstrike=1
    
    global choice_no_of_overs
    for i in range(0,choice_no_of_overs):
        while True:
            b=opponent_team[random.randint(0,10)]
            if b!=bowler:
                bowler=b[::]
                break   
            else :
                continue

        print()
        print(Fore.CYAN+'CURRENT BATSMEN ARE: '+Style.RESET_ALL)
        print(batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')
        print(batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        print('')
        print(Fore.GREEN+bowler,' IS BOWLING THE ',i+1,'th OVER'+Style.RESET_ALL)
        print()
        runs_this_over=0
        wickets_this_over=0
        this_over=[]
        j=1

        while j < 7 :
            time.sleep(2)
            runs_this_ball=0
            out=0
            outcomes=[1,2,3,4,5,6,1,2,3,4,5,6,6,4,5,6,6,6,6,'wide','no-ball']
            y=random.randint(0,len(outcomes)-1)
            a=outcomes[y]
            if onstrike==1:
                striker=batsman1
            else:
                striker=batsman2
            print(bowler,'IS BOWLING')

            print(striker,'IS ON STRIKE ')
            if a=='wide':
                print(Fore.RED+'WIDE BALL'+Style.RESET_ALL)
                print(Fore.CYAN+'LOOKS LIKE ',bowler,' HAS PUSHED THIS TOO WIDE'+Style.RESET_ALL)
                print(Fore.CYAN+"HE'LL HAVE TO RE-BOWL THIS ONE"+Style.RESET_ALL)
                runs_this_ball+=1
                a=random.randint(1,6)
                this_over.append('WD')
            if a=='no-ball':                                     
                runs_this_ball+=1 
                out=1                                         #if out is 1 batsman can't get out
                a=random.randint(1,6)
                print(Fore.BLUE+'ENTER A NUMBER FROM 1 TO 6 TO PLAY THIS BALL'+Style.RESET_ALL)      #for free hit
                print(Fore.RED+'NO BALL'+Style.RESET_ALL)
                noball_message=['OH LOOKS LIKE THE BOWLER HAS OVER-STEPPED HERE',
                                'HMMMM, THE UMPIRES HAVE CALLED THIS A NO-BALL, TOO HIGH ABOVE THE WAIST THEY RECKON']
                noball=random.randint(0,1)
                print(Fore.CYAN+noball_message[noball]+Style.RESET_ALL)
                print(Fore.YELLOW+'FREE-HIT COMING UP'+Style.RESET_ALL)
                print(Fore.GREEN+striker,'IS GOING TO FACE THE FREE HIT'+Style.RESET_ALL)
                print('overs: ',i,'.',j-1,sep='')
                try:
                    x=int(input(''))
                except:
                    print(Fore.RED+'Enter valid option'+Style.RESET_ALL)
                    continue
                if x==a:
                    x=0
                print(Fore.GREEN+"",x,'runs scored by',striker,'of the free hit'+Style.RESET_ALL)
                runs_this_ball+=x
                this_over.append('NB'+str(x))
                if onstrike==1:
                    runs_scored_by_batsman1+=x
                    balls_faced_by_batsman1+=1
                    if x%2==1:                                   #for changing strike
                        onstrike=2
                else:
                    runs_scored_by_batsman2+=x
                    balls_faced_by_batsman2+=1
                    if x%2==1:
                        onstrike=1
            
            print(Fore.BLUE+'ENTER A NUMBER FROM 1 TO 6 TO PLAY THIS BALL'+Style.RESET_ALL)
            print('overs: ',i,'.',j-1,sep='')
            while True:
                try:
                    x=int(input(''))
                except:
                    print(Fore.RED+'enter valid option'+Style.RESET_ALL)
                    continue
                if x not in [1,2,3,4,5,6]:
                    print(Fore.RED+'ENTER VALID OPTION from 1 to 6:'+Style.RESET_ALL)
                else:
                    break
            
            if a==x and out==0:
                wickets_this_over+=1
                wickets+=1
                print(Fore.RED+"OH NO! THERE'S A WICKET HERE"+Style.RESET_ALL)
                if j==6 and i==choice_no_of_overs-1:
                    continue
                if onstrike==1:
                    print(Fore.CYAN+batsman1,'IS OUT FOR',runs_scored_by_batsman1,"IN",balls_faced_by_batsman1+1,'BALLS'+Style.RESET_ALL)
                    runs_scored_by_batsman1=0
                    balls_faced_by_batsman1=0
                    out_batsmen.append(batsman1)
                    if wickets==10:
                        print('------------------------------ALL OUT----------------------------------')
                        exit()

                    while True:
                        print(Fore.CYAN+'Batsman left :'+Style.RESET_ALL)
                        for f in my_team:
                            if f!=batsman1 and f!=batsman2 and f not in out_batsmen:
                                print(f,end=', ')
                        print()
                        batsman1=str(input(Fore.BLUE+'ENTER THE NEXT BATSMAN: '+Style.RESET_ALL))
                        if batsman1 in my_team and batsman1 not in out_batsmen and batsman1!=batsman2:
                            print(batsman1,'WALKS UP TO THE CREASE')
                            break
                        else:
                            print(Fore.RED+'Please enter a batsman in the team that is not out'+Style.RESET_ALL)
                            print(Fore.CYAN+'Your team is : ',my_team+Style.RESET_ALL,sep='\n')
                            print(Fore.RED+'Batsman already out are : ',out_batsmen+Style.RESET_ALL,sep='\n')
                runs_this_innings+=runs_this_ball

                if onstrike==2:
                    print(Fore.CYAN+batsman2,'IS OUT FOR',runs_scored_by_batsman2,"IN",balls_faced_by_batsman2+1,'BALLS'+Style.RESET_ALL)
                    runs_scored_by_batsman2=0
                    balls_faced_by_batsman2=0
                    out_batsmen.append(batsman2)
                    if wickets==10:
                        print('------------------------------ALL OUT----------------------------------')
                        exit()

                    while True:
                        print(Fore.CYAN+'Batsman left :'+Style.RESET_ALL)
                        for f in my_team:
                            if f!=batsman1 and f!=batsman2 and f not in out_batsmen:
                                print(f,end=', ')
                        print()
                        batsman2=str(input(Fore.BLUE+'ENTER THE NEXT BATSMAN: '+Style.RESET_ALL))
                        if batsman2 in my_team and batsman2 not in out_batsmen and batsman1!=batsman2:
                            print(Fore.CYAN+batsman2,'WALKS UP TO THE CREASE'+Style.RESET_ALL)
                            break
                        else:
                            print(Fore.RED+'Please enter a batsman in the team that is not out'+Style.RESET_ALL)

                print(Fore.CYAN+'CURRENT BATSMEN ARE: '+Style.RESET_ALL)
                print(batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')
                print(batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
                this_over.append('W')
                runs_this_innings+=runs_this_ball

            else:
                print(x,'runs scored by',striker)
                runs_this_ball+=x
                this_over.append(str(x))
                if onstrike==1:
                    runs_scored_by_batsman1+=x
                    balls_faced_by_batsman1+=1
                    if x%2==1:                                   #for changing strike
                        onstrike=2
                else:
                    runs_scored_by_batsman2+=x
                    balls_faced_by_batsman2+=1
                    if x%2==1:
                        onstrike=1
                runs_this_over+=runs_this_ball
                runs_this_innings+=runs_this_ball
                
            j+=1
            print('')
            if j==7:
                if onstrike==1:
                    onstrike=2
                else:
                    onstrike=1
        print(Fore.YELLOW+'LOADING ...'+Style.RESET_ALL)
        time.sleep(3)
        clear()


        score=str(runs_this_innings) + '-' + str(wickets)
        print('THIS OVER: ')
        for k in this_over:
            print(k,end=' ')
        print('')
        print('THE SCORE IS ',score,'AFTER ',i+1,'.0 overs',sep='')
        print('')
        if onstrike==1:
            print(' * ',batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')               # ' * 'means on strike
            print('   ',batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        else:
            print('   ',batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')
            print(' * ',batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        print('')
        print(bowler,'gave',runs_this_over,'runs this over and took',wickets_this_over,'wickets this over')

    print(Fore.GREEN+'At the end of the first innings score is',score)
    print(Fore.GREEN+'Your opponent team has to score',runs_this_innings+1,'to win in',choice_no_of_overs,
    'overs at',(runs_this_innings+1)/choice_no_of_overs,'runs per over.'+Style.RESET_ALL)
    target=runs_this_innings+1
    print(Fore.GREEN+"THE TARGET FOR THE OPPONENT TEAM IS ",target,"RUNS"+Style.RESET_ALL)
    time.sleep(1)
    print(Fore.YELLOW+'LOADING ...'+Style.RESET_ALL)
    time.sleep(5)
    clear()
    runs_result_list_for_table.append(score)


def bowling_first(): 
    global my_team , opponent_team , target         #so i can access runs of the over and ball in both functions 
    runs_this_innings=0 
    wickets=0 
    out_batsmen=[] 
    runs_scored_by_batsman1=0 
    runs_scored_by_batsman2=0 
    balls_faced_by_batsman1=0 
    balls_faced_by_batsman2=0 
    batsman1=opponent_team[0] 
    batsman2=opponent_team[1]
    bowler='' 
    '''runs_given_by_bowler=0
    bowler_stats={}''' 
    onstrike=1

    global choice_no_of_overs
    for i in range(0,choice_no_of_overs):
        print(Fore.CYAN+'Your team :'+Style.RESET_ALL)
        print(my_team)
        print(Fore.BLUE+'ENTER BOWLER NAME TO BOWL THE',i+1,'th OVER .'+Style.RESET_ALL)
        while True:
            b=str(input(''))
            if b in my_team:
                if b==bowler:
                    print(Fore.RED+"SAME BOWLER CAN'T BOWL CONSECUTIVE OVERS, PLEASE ENTER BOWLER TO BOWL NEXT OVER "+Style.RESET_ALL)
                else :
                    bowler=b[::]
                    break
            else:
                print(Fore.RED+'BOWLER NOT IN TEAM, PLEASE ENTER A PLAYER FROM TEAM'+Style.RESET_ALL)
                print(my_team)
        print()
        print(Fore.CYAN+'CURRENT BATSMEN ARE: '+Style.RESET_ALL)
        print(batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')
        print(batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        print('')
        runs_this_over=0
        wickets_this_over=0
        this_over=[]
        j=1

        while j < 7 :
            time.sleep(2)  
            runs_this_ball=0
            out=0
            outcomes=[0,1,2,3,4,5,6,0,1,2,3,4,5,6,'wide','no-ball']
            y=random.randint(0,len(outcomes)-1)
            a=outcomes[y]
            if onstrike==1:
                striker=batsman1
            else:
                striker=batsman2
            print(Fore.CYAN+bowler,'IS BOWLING'+Style.RESET_ALL)

            print(Fore.GREEN+striker,'IS ON STRIKE '+Style.RESET_ALL)
            if a=='wide':
                print(Fore.RED+'WIDE BALL'+Style.RESET_ALL)
                print(Fore.CYAN+'LOOKS LIKE',bowler,' HAS PUSHED THIS TOO WIDE'+Style.RESET_ALL)
                print(Fore.CYAN+"HE'LL HAVE TO RE-BOWL THIS ONE"+Style.RESET_ALL)
                runs_this_ball+=1
                a=random.randint(1,6)
                this_over.append('WD')
            if a=='no-ball':                                     
                runs_this_ball+=1 
                out=1                                         #if out is 1 batsman can't get out
                a=random.randint(1,6)
                print(Fore.RED+'NO BALL'+Style.RESET_ALL)
                noball_message=['OH LOOKS LIKE THE BOWLER HAS OVER-STEPPED HERE',
                                'HMMMM, THE UMPIRES HAVE CALLED THIS A NO-BALL, TOO HIGH ABOVE THE WAIST THEY RECKON']
                noball=random.randint(0,1)
                print(Fore.CYAN+noball_message[noball])
                print(Fore.YELLOW+'FREE-HIT COMING UP'+Style.RESET_ALL)
                print(Fore.GREEN+"",striker,'IS GOING TO FACE THE FREE HIT'+Style.RESET_ALL)
                print(Fore.BLUE+'ENTER A NUMBER FROM 1 TO 6 TO BOWL THIS BALL'+Style.RESET_ALL)      #for free hit
                print('overs: ',i,'.',j-1,sep='')
                try:
                    x=int(input(''))
                except:
                    print(Fore.RED+'Enter valid option'+Style.RESET_ALL)
                    continue
                if x==a:
                    a=0
                print(Fore.GREEN+"",a,'runs scored by',striker,'of the free hit'+Style.RESET_ALL)
                runs_this_ball+=a
                this_over.append('NB'+str(a))
                if onstrike==1:
                    runs_scored_by_batsman1+=a
                    balls_faced_by_batsman1+=1
                    if a%2==1:                                   #for changing strike
                        onstrike=2
                else:
                    runs_scored_by_batsman2+=a
                    balls_faced_by_batsman2+=1
                    if a%2==1:
                        onstrike=1
                a=random.randint(1,6)
                
            print(Fore.BLUE+'ENTER A NUMBER FROM 1 TO 6 TO BOWL THIS BALL'+Style.RESET_ALL)
            print('overs: ',i,'.',j-1,sep='',end=' ')
            while True:
                try:
                    x=int(input(''))
                except:
                    print(Fore.RED+'Enter valid option'+Style.RESET_ALL)
                    continue
                if x not in [1,2,3,4,5,6]:
                    print(Fore.RED+'ENTER VALID OPTION from 1 to 6:'+Style.RESET_ALL)
                else:
                    break
            
            if a==x and out==0:
                wickets_this_over+=1
                wickets+=1
                print(Fore.RED+"HOW WAS THAT? THERE'S A WICKET THERE!"+Style.RESET_ALL)
                if j==6 and i==choice_no_of_overs-1:
                    continue
                if onstrike==1:
                    print(batsman1,'IS OUT FOR',runs_scored_by_batsman1,"IN",balls_faced_by_batsman1+1,'BALLS')
                    print()
                    runs_scored_by_batsman1=0
                    balls_faced_by_batsman1=0
                    out_batsmen.append(batsman1)
                    if wickets==10:
                        print('------------------------------ALL OUT----------------------------------')
                        exit()
                    while True :
                        batsman1=opponent_team[random.randint(2,10)]
                        if batsman1 not in out_batsmen and batsman1!=batsman2:
                            print(Fore.CYAN+batsman1,'WALKS UP TO THE CREASE'+Style.RESET_ALL)
                            break
                        else :
                            continue
                runs_this_innings+=runs_this_ball

                if onstrike==2:
                    print(batsman2,'IS OUT FOR',runs_scored_by_batsman2,"IN",balls_faced_by_batsman2+1,'BALLS')
                    print()
                    runs_scored_by_batsman2=0
                    balls_faced_by_batsman2=0
                    out_batsmen.append(batsman2)
                    if wickets==10:
                        print('------------------------------ALL OUT----------------------------------')
                        exit()
                    while True :
                        batsman2=opponent_team[random.randint(2,10)]
                        if batsman2 not in out_batsmen and batsman2!=batsman1:
                            print(Fore.CYAN+batsman2,'WALKS UP TO THE CREASE')
                            break
                        else :
                            continue
                print(Fore.CYAN+'CURRENT BATSMEN ARE: '+Style.RESET_ALL)
                print(batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')
                print(batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
                print()
                this_over.append('W')

            else:
                print(a,'runs scored by',striker)
                print()
                runs_this_ball+=a
                this_over.append(str(a))
                if onstrike==1:
                    runs_scored_by_batsman1+=a
                    balls_faced_by_batsman1+=1
                    if a%2==1:                                   #for changing strike
                        onstrike=2
                else:
                    runs_scored_by_batsman2+=a
                    balls_faced_by_batsman2+=1
                    if a%2==1:
                        onstrike=1
                runs_this_over+=runs_this_ball
                runs_this_innings+=runs_this_ball

            j+=1
            if j==7:
                if onstrike==1:
                    onstrike=2
                else:
                    onstrike=1
        print(Fore.YELLOW+'LOADING ...'+Style.RESET_ALL)
        time.sleep(3)
        clear()

        score=str(runs_this_innings) + '-' + str(wickets)
        print('THIS OVER: ')
        for k in this_over:
            print(k,end=' ')
        print('')
        print('THE SCORE IS ',score,' AFTER ',i+1,'.0 overs',sep='')
        print('')
        if onstrike==1:
            print(' * ',batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')               # ' * 'means on strike
            print('   ',batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        else:
            print('   ',batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')
            print(' * ',batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        print('')
        print(bowler,'gave',runs_this_over,'runs this over and took',wickets_this_over,'wickets this over')



    print(Fore.CYAN+'At the end of the first innings score is',score)
    print('Your team has to score',runs_this_innings+1,'to win in',choice_no_of_overs,
            'overs at',(runs_this_innings+1)/choice_no_of_overs,'runs per over.'+Style.RESET_ALL)
    target=runs_this_innings+1
    print(Fore.YELLOW+'LOADING ...'+Style.RESET_ALL)
    time.sleep(5)
    clear()
    runs_result_list_for_table.append(score)


def batting_second():
    global my_team , opponent_team , target , win                                            #so i can access runs of the over and ball in both functions
    runs_this_innings=0
    wickets=0
    out_batsmen=[]
    runs_scored_by_batsman1=0
    runs_scored_by_batsman2=0
    balls_faced_by_batsman1=0
    balls_faced_by_batsman2=0
    batsman1=my_team[0]
    batsman2=my_team[1]
    bowler=''
    #runs_given_by_bowler=0
    onstrike=1
    runs_left_to_chase=target
    
    
    global choice_no_of_overs
    balls_to_spare=choice_no_of_overs*6
    print(Fore.CYAN+'YOUR OPPONENT HAS PUT UP A TOTAL OF ',target,' RUNS FOR YOU TO CHASE '+Style.RESET_ALL)
    print("LET'S SEE IF YOU CAN CHASE THIS DOWN "+Style.RESET_ALL)
    for i in range(0,choice_no_of_overs):
        if win==1:
            break
        while True:
            b=opponent_team[random.randint(0,10)]
            if b!=bowler:
                bowler=b[::]
                break   
            else :
                continue
            
        print()
        print(Fore.CYAN+'CURRENT BATSMEN ARE: '+Style.RESET_ALL)
        print(batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')
        print(batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        print('')
        print(bowler,' IS BOWLING THE ',i+1,'th OVER')
        print()
        runs_this_over=0
        wickets_this_over=0
        this_over=[]
        j=1

        while j < 7 :
            time.sleep(2) 
            runs_this_ball=0
            out=0
            outcomes=[1,2,3,4,5,6,1,2,3,4,5,6,6,'wide','no-ball']
            y=random.randint(0,len(outcomes)-1)
            a=outcomes[y]
            if onstrike==1:
                striker=batsman1
            else:
                striker=batsman2
            
            print(bowler,'IS BOWLING')
            print(striker,'IS ON STRIKE ')

            if a=='wide':
                print(Fore.RED+'WIDE BALL'+Style.RESET_ALL)
                print(Fore.CYAN+'LOOKS LIKE ',bowler,' HAS PUSHED THIS TOO WIDE')
                print("HE'LL HAVE TO RE-BOWL THIS ONE"+Style.RESET_ALL)
                runs_this_ball+=1
                a=random.randint(1,6)
                this_over.append('WD')
                if runs_left_to_chase-1==0:
                    runs_this_innings+=1
                    print(Fore.GREEN+'You won'+Style.RESET_ALL)  
                    win=1                           #if runs to chase is 0 you finished the chase
                    break
            if a=='no-ball':                                     
                runs_this_ball+=1 
                out=1                                         #if out is 1 batsman can't get out
                a=random.randint(1,6)
                print(Fore.BLUE+'ENTER A NUMBER FROM 1 TO 6 TO PLAY THIS BALL'+Style.RESET_ALL)      #for free hit
                print(Fore.RED+'NO BALL'+Style.RESET_ALL)
                noball_message=['OH LOOKS LIKE THE BOWLER HAS OVER-STEPPED HERE',
                                'HMMMM, THE UMPIRES HAVE CALLED THIS A NO-BALL, TOO HIGH ABOVE THE WAIST THEY RECKON']
                noball=random.randint(0,1)
                print(Fore.CYAN+noball_message[noball]+Style.RESET_ALL)
                print(Fore.YELLOW+'FREE-HIT COMING UP'+Style.RESET_ALL)
                print(Fore.GREEN+"",striker,'IS GOING TO FACE THE FREE HIT'+Style.RESET_ALL)
                print('overs: ',i,'.',j-1,sep='')
                try:
                    x=int(input(''))
                except:
                    print(Fore.RED+'Enter valid option'+Style.RESET_ALL)
                    continue
                if x==a:
                    x=0
                print(Fore.GREEN+"",x,'runs scored by',striker,'of the free hit'+Style.RESET_ALL)
                runs_this_ball+=x
                this_over.append('NB'+str(x))
                if runs_left_to_chase<x:
                    runs_this_over+=runs_this_ball
                    runs_this_innings+=runs_this_ball
                    runs_left_to_chase-=runs_this_ball
                    if runs_left_to_chase-1<=0:
                        print(Fore.GREEN+'You won'+Style.RESET_ALL)
                        win=1
                        break

                if onstrike==1:
                    runs_scored_by_batsman1+=x
                    balls_faced_by_batsman1+=1
                    if x%2==1:                                   #for changing strike
                        onstrike=2
                else:
                    runs_scored_by_batsman2+=x
                    balls_faced_by_batsman2+=1
                    if x%2==1:
                        onstrike=1
                if runs_left_to_chase-1==0:
                    print(Fore.GREEN+'You won'+Style.RESET_ALL)  
                    win=1                         #if runs to chase is 0 you finished the chase
                    break

            print(Fore.BLUE+'ENTER A NUMBER FROM 1 TO 6 TO PLAY THIS BALL'+Style.RESET_ALL)
            print('overs: ',i,'.',j-1,sep='')
            while True:
                try:
                    x=int(input(''))
                except:
                    print(Fore.RED+'Enter valid option'+Style.RESET_ALL)
                    continue
                if x not in [1,2,3,4,5,6]:
                    print(Fore.RED+'ENTER VALID OPTION from 1 to 6:'+Style.RESET_ALL)
                else:
                    break
            
            if a==x and out==0:
                wickets_this_over+=1
                wickets+=1
                print(Fore.RED+"OH NO! THERE'S A WICKET HERE"+Style.RESET_ALL)
                if j==6 and i==choice_no_of_overs-1:
                    continue
                if onstrike==1:
                    print(batsman1,'IS OUT FOR',runs_scored_by_batsman1,"IN",balls_faced_by_batsman1+1,'BALLS')
                    runs_scored_by_batsman1=0
                    balls_faced_by_batsman1=0
                    out_batsmen.append(batsman1)
                    if wickets==10:
                        print('------------------------------ALL OUT----------------------------------')
                        exit()

                    while True:
                        print(Fore.CYAN+'Batsman left :'+Style.RESET_ALL)
                        for f in my_team:
                            if f!=batsman1 and f!=batsman2 and f not in out_batsmen:
                                print(f,end=', ')
                        print()
                        batsman1=str(input(Fore.BLUE+'ENTER THE NEXT BATSMAN: '+Style.RESET_ALL))
                        if batsman1 in my_team and batsman1 not in out_batsmen and batsman1!=batsman2:
                            print(Fore.CYAN+batsman1,'WALKS UP TO THE CREASE'+Style.RESET_ALL)
                            break
                        else:
                            print(Fore.RED+'Please enter a batsman in the my_team that is not out'+Style.RESET_ALL)
                            print(Fore.CYAN+'Your team is : ',my_team,sep='\n')
                            print(Fore.RED+'Batsman already out are : ',out_batsmen,sep='\n')
                runs_this_innings+=runs_this_ball

                if onstrike==2:
                    print(batsman2,'IS OUT FOR',runs_scored_by_batsman2,"IN",balls_faced_by_batsman2+1,'BALLS')
                    runs_scored_by_batsman2=0
                    balls_faced_by_batsman2=0
                    out_batsmen.append(batsman2)
                    if wickets==10:
                        print('------------------------------ALL OUT----------------------------------')
                        exit()

                    while True:
                        print(Fore.CYAN+'Batsman left :'+Style.RESET_ALL)
                        for f in my_team:
                            if f!=batsman1 and f!=batsman2 and f not in out_batsmen:
                                print(f,end=', ')
                        print()
                        batsman2=str(input(Fore.BLUE+'ENTER THE NEXT BATSMAN: '+Style.RESET_ALL))
                        if batsman2 in my_team and batsman2 not in out_batsmen and batsman1!=batsman2:
                            print(Fore.CYAN+batsman2,'WALKS UP TO THE CREASE'+Style.RESET_ALL)
                            break
                        else:
                            print(Fore.RED+'Please enter a batsman in the team that is not out'+Style.RESET_ALL)

                print(Fore.CYAN+'CURRENT BATSMEN ARE: '+Style.RESET_ALL)
                print(batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')
                print(batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
                this_over.append('W')

            else:
                print(x,'runs scored by',striker)
                runs_this_ball+=x
                this_over.append(str(x))
                if onstrike==1:
                    runs_scored_by_batsman1+=x
                    balls_faced_by_batsman1+=1
                    if x%2==1:                                   #for changing strike
                        onstrike=2
                else:
                    runs_scored_by_batsman2+=x
                    balls_faced_by_batsman2+=1
                    if x%2==1:
                        onstrike=1
                runs_this_over+=runs_this_ball
                runs_this_innings+=runs_this_ball
                runs_left_to_chase-=runs_this_ball
                if runs_left_to_chase<=0:
                    win=1
                    break

            j+=1
            balls_to_spare-=1
            print('')
            if j==7:
                if onstrike==1:
                    onstrike=2
                else:
                    onstrike=1

        print(Fore.YELLOW+'LOADING ...'+Style.RESET_ALL)
        time.sleep(3)
        if win!=1:
            clear()

        score=str(runs_this_innings) + '-' + str(wickets)
        print(Fore.CYAN+'THIS OVER: '+Style.RESET_ALL)
        for k in this_over:
            print(k,end=' ')
        print('')
        if win==1:
            break
        print('THE SCORE IS ',score,'AFTER ',i+1,'.0 overs',sep='')
        print('')
        if onstrike==1:
            print(' * ',batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')               # ' * 'means on strike
            print('   ',batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        else:
            print('   ',batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')
            print(' * ',batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        print('')
        print(bowler,'gave',runs_this_over,'runs this over and took',wickets_this_over,'wickets this over')
        print()
        if i==choice_no_of_overs-1 and runs_this_innings==target-1:
            result='DRAW MATCH'
            print(Fore.CYAN+'SCORES LEVEL GAME IS TIED, WHAT A THRILLER OF A GAME'+Style.RESET_ALL)
            print()
            print(Fore.CYAN+"You have earned 20 coins"+Style.RESET_ALL)
            print()
            earn="update LOGIN set coins=coins+20 where username='{}'".format(uname)
            m.execute(earn)
            conn.commit()
        elif i==choice_no_of_overs-1 and runs_this_innings!=target-1:
            result="YOU LOST BY " + runs_left_to_chase-1 + "RUNS"
            print(Fore.RED+'BETTER LUCK NEXT TIME, YOU LOST BY ',runs_left_to_chase-1,'RUNS'+Style.RESET_ALL)
            print()
            print(Fore.CYAN+"You have earned 5 coins"+Style.RESET_ALL)
            print()
            earn="update LOGIN set coins=coins+5 where username='{}'".format(uname)
            m.execute(earn)
            conn.commit()
        else:
            print(Fore.CYAN+'YOU NEED TO SCORE ',runs_left_to_chase,' IN ',choice_no_of_overs-i-1,
                ' OVERS AT A REQUIRED RUN RATE OF ',runs_left_to_chase/(choice_no_of_overs-i-1),' RUNS PER OVER'+Style.RESET_ALL)

    if win==1:
        print(Fore.GREEN+'YOU WON THE MATCH CONGRATULATIONS!!!!'+Style.RESET_ALL)
        print()
        print(Fore.CYAN+"You have earned 40 coins"+Style.RESET_ALL)
        print()
        earn="update LOGIN set coins=coins+40 where username='{}'".format(uname)
        m.execute(earn)
        conn.commit()
        if onstrike==1:
            print(' * ',batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')               # ' * 'means on strike
            print('   ',batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        else:
            print('   ',batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')
            print(' * ',batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        print()
        result='YOU WON THE MATCH BY ' + str(10-wickets) + ' WICKETS, WITH ' + str(balls_to_spare-1) + ' BALLS TO SPARE'
        print(Fore.GREEN+result+Style.RESET_ALL)

    print(Fore.CYAN+'At the end of the second innings your score is',score)
    print(Fore.CYAN+"Your opponent team's score was ",target-1,'after',choice_no_of_overs,'overs'+Style.RESET_ALL)
    print(Fore.YELLOW+'LOADING ...'+Style.RESET_ALL)
    time.sleep(10)
    clear()
    runs_result_list_for_table.append(score)
    runs_result_list_for_table.append(result)


def bowling_second():
    global my_team , opponent_team , target , win                                            #so i can access runs of the over and ball in both functions
    runs_this_innings=0 
    wickets=0 
    out_batsmen=[] 
    runs_scored_by_batsman1=0 
    runs_scored_by_batsman2=0 
    balls_faced_by_batsman1=0 
    balls_faced_by_batsman2=0 
    batsman1=opponent_team[0] 
    batsman2=opponent_team[1]
    bowler=''
    onstrike=1
    runs_left_to_chase=target
    
    
    global choice_no_of_overs
    balls_to_spare=choice_no_of_overs*6
    print(Fore.CYAN+'YOU HAVE SET YOUR OPPONENT A TARGET OF ',target,' RUNS TO CHASE '+Style.RESET_ALL)
    print(Fore.CYAN+"LET'S SEE IF YOU CAN DEFEND THIS TOTAL "+Style.RESET_ALL)
    for i in range(0,choice_no_of_overs):
        if win==1:
            break
        print(Fore.CYAN+'Your team :')
        print(my_team)
        print(Fore.BLUE+'ENTER BOWLER NAME TO BOWL THE',i+1,'th OVER .'+Style.RESET_ALL)
        while True:
            b=str(input(''))
            if b in my_team:
                if b==bowler:
                    print(Fore.RED+"SAME BOWLER CAN'T BOWL CONSECUTIVE OVERS, PLEASE ENTER BOWLER TO BOWL NEXT OVER "+Style.RESET_ALL)
                else :
                    bowler=b[::]
                    break
            else:
                print(Fore.RED+'BOWLER NOT IN TEAM, PLEASE ENTER A PLAYER FROM TEAM'+Style.RESET_ALL)
                print(my_team)
        print()
        print(Fore.CYAN+'CURRENT BATSMEN ARE: '+Style.RESET_ALL)
        print(batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')
        print(batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        print('')
        runs_this_over=0
        wickets_this_over=0
        this_over=[]
        j=1

        while j < 7 :
            time.sleep(2)  
            runs_this_ball=0
            out=0
            outcomes=[0,1,2,3,4,5,6,0,1,2,3,4,5,6,'wide','no-ball']
            y=random.randint(0,len(outcomes)-1)
            a=outcomes[y]
            if onstrike==1:
                striker=batsman1
            else:
                striker=batsman2
            print(bowler,'IS BOWLING')

            print(striker,'IS ON STRIKE ')
            if a=='wide':
                print(Fore.RED+'WIDE BALL'+Style.RESET_ALL)
                print(Fore.CYAN+'LOOKS LIKE',bowler,' HAS PUSHED THIS TOO WIDE')
                print(Fore.CYAN+"HE'LL HAVE TO RE-BOWL THIS ONE"+Style.RESET_ALL)
                runs_this_ball+=1
                a=random.randint(1,6)
                this_over.append('WD')
                if runs_left_to_chase-1==0:
                    runs_this_innings+=1
                    print('You lose')  
                    win=1                           #if runs to chase is 0 you finished the chase
                    break
            if a=='no-ball':                                     
                runs_this_ball+=1 
                out=1                                         #if out is 1 batsman can't get out
                a=random.randint(1,6)
                print(Fore.RED+'NO BALL')
                noball_message=['OH LOOKS LIKE THE BOWLER HAS OVER-STEPPED HERE',
                                'HMMMM, THE UMPIRES HAVE CALLED THIS A NO-BALL, TOO HIGH ABOVE THE WAIST THEY RECKON']
                noball=random.randint(0,1)
                print(Fore.CYAN+noball_message[noball]+Style.RESET_ALL)
                print(Fore.YELLOW+'FREE-HIT COMING UP'+Style.RESET_ALL)
                print(Fore.GREEN+striker,'IS GOING TO FACE THE FREE HIT'+Style.RESET_ALL)
                print(Fore.BLUE+'ENTER A NUMBER FROM 1 TO 6 TO BOWL THIS BALL'+Style.RESET_ALL)      #for free hit
                print('overs: ',i,'.',j-1,sep='')
                try:
                    x=int(input(''))
                except:
                    print(Fore.RED+'Enter valid option'+Style.RESET_ALL)
                    continue
                if x==a:
                    a=0
                print(Fore.GREEN+"",a,'runs scored by',striker,'of the free hit'+Style.RESET_ALL)
                runs_this_ball+=a
                this_over.append('NB'+str(a))
                if runs_left_to_chase<x:
                    runs_this_over+=runs_this_ball
                    runs_this_innings+=runs_this_ball
                    runs_left_to_chase-=runs_this_ball
                    if runs_left_to_chase-1<=0:
                        print(Fore.RED+'You lose'+Style.RESET_ALL)
                        win=1
                        break

                if onstrike==1:
                    runs_scored_by_batsman1+=a
                    balls_faced_by_batsman1+=1
                    if a%2==1:                                   #for changing strike
                        onstrike=2
                else:
                    runs_scored_by_batsman2+=a
                    balls_faced_by_batsman2+=1
                    if a%2==1:
                        onstrike=1
                a=random.randint(1,6)

                if runs_left_to_chase-1==0:
                    print(Fore.RED+'You lose'+Style.RESET_ALL)  
                    win=1                         #if runs to chase is 0 you finished the chase
                    break

            print(Fore.BLUE+'ENTER A NUMBER FROM 1 TO 6 TO BOWL THIS BALL'+Style.RESET_ALL)
            print('overs: ',i,'.',j-1,sep='',end=' ')
            while True:
                try:
                    x=int(input(''))
                except:
                    print(Fore.RED+'Enter valid option'+Style.RESET_ALL)
                    continue
                if x not in [1,2,3,4,5,6]:
                    print(Fore.RED+'ENTER VALID OPTION from 1 to 6:'+Style.RESET_ALL)
                else:
                    break
            
            if a==x and out==0:
                wickets_this_over+=1
                wickets+=1
                print(Fore.RED+"HOW WAS THAT? THERE'S A WICKET THERE!"+Style.RESET_ALL)
                if j==6 and i==choice_no_of_overs-1:
                    continue
                if onstrike==1:
                    print(batsman1,'IS OUT FOR',runs_scored_by_batsman1,"IN",balls_faced_by_batsman1+1,'BALLS')
                    print()
                    runs_scored_by_batsman1=0
                    balls_faced_by_batsman1=0
                    out_batsmen.append(batsman1)
                    if wickets==10:
                        print(Fore.RED+'------------------------------ALL OUT----------------------------------')
                        exit()

                    while True :
                        batsman1=opponent_team[random.randint(2,10)]
                        if batsman1 not in out_batsmen and batsman1!=batsman2:
                            print(Fore.CYAN+batsman1,'WALKS UP TO THE CREASE'+Style.RESET_ALL)
                            break
                        else :
                            continue
                runs_this_innings+=runs_this_ball

                if onstrike==2:
                    print(batsman2,'IS OUT FOR',runs_scored_by_batsman2,"IN",balls_faced_by_batsman2+1,'BALLS')
                    runs_scored_by_batsman2=0
                    balls_faced_by_batsman2=0
                    out_batsmen.append(batsman2)
                    if wickets==10:
                        print('------------------------------ALL OUT----------------------------------')
                        exit()

                    while True :
                        batsman2=opponent_team[random.randint(2,10)]
                        if batsman2 not in out_batsmen and batsman2!=batsman1:
                            print(Fore.CYAN+batsman2,'WALKS UP TO THE CREASE'+Style.RESET_ALL)
                            break
                        else :
                            continue
                print(Fore.CYAN+'CURRENT BATSMEN ARE: '+Style.RESET_ALL)
                print(batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')
                print(batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
                this_over.append('W')

            else:
                print(a,'runs scored by',striker)
                runs_this_ball+=a
                this_over.append(str(a))
                if onstrike==1:
                    runs_scored_by_batsman1+=a
                    balls_faced_by_batsman1+=1
                    if a%2==1:                                   #for changing strike
                        onstrike=2
                else:
                    runs_scored_by_batsman2+=a
                    balls_faced_by_batsman2+=1
                    if a%2==1:
                        onstrike=1
                runs_this_over+=runs_this_ball
                runs_this_innings+=runs_this_ball
                runs_left_to_chase-=runs_this_ball
                if runs_left_to_chase<=0:
                    print(Fore.RED+'you lose'+Style.RESET_ALL)
                    win=1
                    break
                
            j+=1
            balls_to_spare-=1
            print('')
            if j==7:
                if onstrike==1:
                    onstrike=2
                else:
                    onstrike=1
        print(Fore.YELLOW+'LOADING ...'+Style.RESET_ALL)
        time.sleep(3)
        if win!=1:
            clear()

        score=str(runs_this_innings) + '-' + str(wickets)
        print(Fore.CYAN+'THIS OVER: '+Style.RESET_ALL)
        for k in this_over:
            print(k,end=' ')
        print('')
        if win==1:
            break
        print('THE SCORE IS ',score,'AFTER ',i+1,'.0 overs',sep='')
        print('')

        if onstrike==1:
            print(' * ',batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')               # ' * 'means on strike
            print('   ',batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        else:
            print('   ',batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')
            print(' * ',batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        print('')
        print(bowler,'gave',runs_this_over,'runs this over and took',wickets_this_over,'wickets this over')
        print()
        if i==choice_no_of_overs-1 and runs_this_innings==target-1:
            result='DRAW MATCH'
            print(Fore.CYAN+'SCORES LEVEL GAME IS TIED, WHAT A THRILLER OF A GAME'+Style.RESET_ALL)
            print()
            print(Fore.CYAN+"You have earned 20 coins"+Style.RESET_ALL)
            print()
            earn="update LOGIN set coins=coins+20 where username='{}'".format(uname)
            m.execute(earn)
            conn.commit()
            print()
        elif i==choice_no_of_overs-1 and runs_this_innings!=target-1:
            print(Fore.GREEN+'YOU WON THE MATCH CONGRATULATIONS!!!!'+Style.RESET_ALL)
            print()
            result= "YOU WON BY " + str(runs_left_to_chase-1) + ' RUNS'
            print(Fore.GREEN+"LET'S GO, YOU WON BY ",runs_left_to_chase-1,'RUNS'+Style.RESET_ALL)
            print()
            print(Fore.CYAN+"You have earned 40 coins"+Style.RESET_ALL)
            print()
            earn="update LOGIN set coins=coins+40 where username='{}'".format(uname)
            m.execute(earn)
            conn.commit()
        else:
            print(Fore.CYAN+'YOU NEED TO DEFEND ',runs_left_to_chase,' IN ',choice_no_of_overs-i-1,
                ' OVERS AND CONTAIN A REQUIRED RUN RATE OF LESS THAN ',runs_left_to_chase/(choice_no_of_overs-i-1),' RUNS PER OVER'+Style.RESET_ALL)

    if win==1:
        print(Fore.RED+'BETETR LUCK NEXT TIME, YOU LOST THIS GAME'+Style.RESET_ALL)
        print()
        if onstrike==1:
            print(' * ',batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')               # ' * 'means on strike
            print('   ',batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        else:
            print('   ',batsman1,' ',runs_scored_by_batsman1,'(',balls_faced_by_batsman1,')',sep='')
            print(' * ',batsman2,' ',runs_scored_by_batsman2,'(',balls_faced_by_batsman2,')',sep='')
        print()
        result='YOUR OPPONENT WON THE MATCH BY ' + str(10-wickets) + ' WICKETS, WITH ' + str(balls_to_spare-1) + ' BALLS TO SPARE'
        print(Fore.RED+result+Style.RESET_ALL)
        earn="update LOGIN set coins=coins+5 where username='{}'".format(uname)
        m.execute(earn)
        conn.commit()
        print(Fore.CYAN+"You have earned 5 coins"+Style.RESET_ALL)
        print()
    
    print(Fore.CYAN+"At the end of the second innings your opponents' score is",score+Style.RESET_ALL)
    print(Fore.CYAN+"Your team's score was ",target-1,'after',choice_no_of_overs,'overs'+Style.RESET_ALL)
    print(Fore.YELLOW+'LOADING ...'+Style.RESET_ALL)
    time.sleep(10)
    clear()
    runs_result_list_for_table.append(score)
    runs_result_list_for_table.append(result)


clear()
print(Fore.CYAN+'HELLO CRICKETER'+Style.RESET_ALL)                                                 #TO CHOOSE GAME DURATION
print(Fore.GREEN+'THANK YOU FOR PLAYING THIS GAME'+Style.RESET_ALL)
print()
print(Fore.BLUE+'PLEASE ENTER THE GAME DURATION YOU WANT TO PLAY'+Style.RESET_ALL)
print()
print(Fore.GREEN+'-------------------------------------------CHOICES----------------------------------------------'+Style.RESET_ALL)
print()
print(Fore.CYAN+'CHOOSE HOW MANY OVERS GAME YOU WANT TO PLAY '+Style.RESET_ALL)

while True:
    try:
        choice_no_of_overs=int(input(Fore.BLUE+'ENTER CHOICE: '+Style.RESET_ALL))
    except:
        print(Fore.RED + 'Invalid option provided!' + Style.RESET_ALL)
        continue
    if choice_no_of_overs in range(1,5):                    #GAME DURATION 1 TO 4 OVERS
        break
    else:
        print(Fore.RED + 'INVALID INPUT','ENTER A VALID GAME DURATION 1 OVER(SUPER OVER) TO 4 OVER(T4 GAME) ' + Style.RESET_ALL,sep='\n')
print('')
print(Fore.YELLOW+'LOADING ...'+Style.RESET_ALL)
time.sleep(3)



#here you have to enter my_team name extracted from login details 
#my_team also to be extracted form login details
#or squad can be selected
#print('please select your squad')
#we'll try to make the selection of squad later based on a on screen selection

'''opponent_team=['stoinis', 'dhawan', 'iyer', 'rahane', 'pant', 'hetmyr', 'axar', 'pravin', 'rabada', 'ashwin', 'norte']
my_team=['rohit', 'decock', 'virat', 'sky', 'abd', 'kishan', 'pollard', 'pandya', 'boult', 'chahal', 'bumrah']'''
team_selection()
toss(captain)

clear()
print(Fore.CYAN+'ARE YOU READY TO START THE GAME'+Style.RESET_ALL)
print(Fore.GREEN+'LETS PLAY'+Style.RESET_ALL)
print(Fore.YELLOW+'LOADING ...'+Style.RESET_ALL)
time.sleep(3)
print(Fore.CYAN+'Opponent team is : '+Style.RESET_ALL)
print(opponent_team)
print()


if bat_bowl_choice==1:
    batting_first()
    print()
    print()
    bowling_second()
    st="insert into {}(YOUR_BATTING,YOUR_BOWLING,RESULT) values('{}','{}','{}')".format(table_name,runs_result_list_for_table[0],runs_result_list_for_table[1],runs_result_list_for_table[2])
    m.execute(st)
    conn.commit()

else:
    bowling_first()
    print()
    print()
    batting_second()
    st="insert into {}(YOUR_BATTING,YOUR_BOWLING,RESULT) values('{}','{}','{}')".format(table_name,runs_result_list_for_table[1],runs_result_list_for_table[0],runs_result_list_for_table[2])
    m.execute(st)
    conn.commit()

