import json,os
user_choice=input("enter 1 for sign-up and 2 for log-in:-")
if user_choice=="1":
    user_name=input("enter your name:-")
    def main():
        password1=input("enter your password:-")
        a=0
        b=0
        c=0
        d=0
        capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        smallalphabets="abcdefghijklmnopqrstuvwxyz"
        specialcharacters="@&!_#?"
        digits="0123456789"
        if (len(password1)>=6) and len(password1)<=11:
            for i in password1:
                if (i in capitalalphabets):
                    a=a+1
                if (i in smallalphabets):
                    b=b+1
                if (i in specialcharacters):
                    c=c+1
                if (i in digits):
                    d=d+1
            if (a>=1 and b>=1 and c>=1 and d>=1 and (a+b+c+d)==len(password1)):
                print("strong paasword")
            else:
                print("simple password")
            password2=input("conform password:-")
            if password1==password2:
                print("conform password")
                if(os.path.isfile("login_code.json")):
                    file_name=open("login_code.json","r+")
                    a=json.load(file_name)
                    for i in a["user"]:
                        if i["username"]==user_name:
                            print("this file already exist")
                            break
                    else:
                        dic={}
                        d={}
                        l=[]
                        dic["username"]=user_name
                        dic["password"]=password1
                        d["Description"]=input("enter your Description:-")
                        d["D.O.B"]=input("enter your D.O.B:-")
                        d["Gender"]=input("enter your gender:-")
                        d["Hobbies"]=input("enter your hobbies:-")
                        dic["profile"]=d
                        v=a["user"]
                        v.append(dic)
                        f=open("login_code.json","w+")
                        json.dump(a,f,indent=4)
                        f.close()
                        print("Signup successful!")
                else:
                    dic={}
                    d={}
                    l=[]
                    d1={}
                    dic["username"]=user_name
                    dic["password"]=password1
                    d["Description"]=input("enter your Description:-")
                    d["D.O.B"]=input("enter your D.O.B:-")
                    d["Gender"]=input("enter your gender:-")
                    d["Hobbies"]=input("enter your hobbies:-")
                    dic["profile"]=d
                    l.append(dic)
                    d1["user"]=l
                    f=open("login_code.json","w+")
                    json.dump(d1,f,indent=4)
                    f.close()
                    print("Signup successful!")
            else:
                    print("password not match")
        else:
            print("password length must be between 6 and 10")
    main()
elif user_choice=="2":
        x=open("login_code.json","r")
        n=json.load(x)
        name=input("enter the name")
        pws=input("enter password..")
        for i in n["user"]:
            if i["username"]==name:
                if pws==i["password"]:
                    print("login successfully!")
                    print(i["profile"])
                    break
                else:
                    print("check password")
            else:
                print("check user name")
        else:
            print("user not exists??????????????")

