import json
def sign_up():
    user_name=input("enter user name")
    a=0
    b=0
    c=0
    d=0
    user_password=input("enter the passsword:")
    capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets="abcdefghijklmnopqrstuvwxyz"
    specialcharacters="@&!_#?"
    digits="0123456789"
    if (len(user_password)>=6) and len(user_password)<=11:
        for i in user_password:
            if (i in capitalalphabets):
                a=a+1
            if (i in smallalphabets):
                b=b+1
            if (i in specialcharacters):
                c=c+1
            if (i in digits):
                d=d+1
        if (a>=1 and b>=1 and c>=1 and d>=1 and (a+b+c+d)==len(user_password)):
            print("strong paasword")
        else:
            print("simple password")
    else:
        print("password length at least 5")
    password=input("enter your user_password..")
    if password==user_password:
            print("conform password")
            about_me=input("enter about your")
            dath_of_birth=input("enter your dath of birth")
            Gender=input("enter your gender")
            hobbies=input("enter you hobbies")
            dic={}
            dic12={}
            a=[]
            f={}
            dic["description"]=about_me
            dic["D.O.B"]=dath_of_birth
            dic["Gender"]=Gender
            dic["Hobbies"]=hobbies
            f["user_name"]=user_name
            f["password"]=user_password
            f["profile"]=dic
            a.append(f)
            dic12["user"]=a
            print(dic12)
            print("successfully signup")
            x=open("login_practice.json","w")
            json.dump(dic12,x,indent=2)
    else:
        print("wrong password")
def login():
        x=open("login_practice.json","r")
        n=json.load(x)
        name=input("enter the name")
        pws=input("enter password..")
        if name in n["user"][0]["user_name"]:
            if pws in n["user"][0]["password"]:
                print("login successfully!")
            else:
                print("check password")
        else:
            print("check name")
def main():
    print("login")
    print("signup")
    choose=input("enter your choice..")
    if choose=="login":
        n=login()
    elif choose=="signup":
        m=sign_up()
    else:
        print("enter valid choice")
        x=main()
main()
        
    