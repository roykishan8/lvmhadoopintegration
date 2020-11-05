import os
os.system("tput setaf 3")
print("\t\t\tWelcome to my Menu !!")
os.system("tput setaf 7")
print("\t\t\t------------------------")
boole=True
print("hello kishan")
print()
exit=True
while(exit):
    os.system("clear")
    os.system("tput setaf 3")
    print("\t\t\tWelcome to my Menu !!")
    os.system("tput setaf 7")
    print("\t\t\t------------------------")
    boole=True
    print("hello kishan")
    print()
    print("\t\t\t1.Configure a new lvm storage ")
    print("\t\t\t2.Increase the size of lvm storage")
    print("\t\t\t3.Reduce the size of lvm storage")
    print("\t\t\t4.Mount the newly created storage")
    print("\t\t\t5.To see all the mounted disk")
    print("\t\t\t6.To display volume group")
    print("\t\t\t7.To display Logical volume")
    print("\t\t\t8.All hardrive list connected to system")
    print("\t\t\t9.exit")
    boole=True
    a=int(input("ENTER YOUR OPTION : "))
    while(boole==True):
        if(a==1):
            os.system("fdisk -l")
            num=int(input("enter the number of pendrive or hardrive want to join: "))
            num1=num
            l=[]
            while(num>0):
                c=input("Enter the storage name : ")
                l.append(c)
                num=num-1
            for i in range (0,num1):
                os.system("pvcreate {}".format(l[i]))
            print("physical volume created")
            vgname=input("Enter the volume group name: ")
            syntax=""
            for i in l:
                syntax+=i+" "
            os.system("vgcreate {} {}".format(vgname,syntax))
            print("volume group created")
            os.system("vgdisplay {}".format(vgname))
            print()
            lvmsize=int(input("Enter the logical volume size you want to create : "))
            lvmname=input("Enter the name of logical volume you want to keep : ")
            print("creating the logical volume of size-{} GIB with name- {}".format(lvmsize,lvmname))
            os.system("lvcreate --size {}G --name {} {}".format(lvmsize,lvmname,vgname))
            print("\t\t\tHurray !!!!!!!! LVM of size-{}GB with name- {} created successfully".format(lvmsize,lvmname))
            os.system("lvdisplay")
            print()
            input("press enter for main menu: ")
            break
        elif(a==2):
            
            vgname=input("Enter the name of Volume Group: ")
            lvname=input("Enter the name of logical volume group: ")
            os.system("vgdisplay {}".format(vgname))
            size=int(input("Enter the storage you want more in GB : "))

            os.system("lvextend --size +{}G /dev/{}/{}".format(size,vgname,lvname))
            os.system("resize2fs /dev/{}/{}".format(vgname,lvname))
            os.system("lvdisplay")
            print()
            print("\t\t\tsuccessfully extended")
            os.system("df -h")
            input("Press enter to main menu: ")
            break
        elif(a==3):
            
            vgname=input("Enter the name of volume group: ")
            lvname=input("Enter the name of logical volume group: ")
            mdir=input("Enter the mounted drive location: ")
            os.system("lvdisplay")
            size=int(input("Enter the size you actually want to reduce to : "))
            print("unmounting the logical volume")
            os.system("hadoop-daemon.sh stop datanode")
            os.system("umount /dev/{}/{}".format(vgname,lvname))
            os.system("e2fsck -f /dev/{}/{}".format(vgname,lvname))
            os.system("resize2fs /dev/{}/{} {}G".format(vgname,lvname,size))
            os.system("lvreduce -L {}G /dev/{}/{}".format(size,vgname,lvname))
            print("mounting the new shrinked volume to drive: {} ")
            os.system("mount /dev/{}/{} {}".format(vgname,lvname,mdir))
            os.system("lvdisplay")
            print("mounted shrinked volume: ")
            os.system("hadoop-daemon.sh start datanode")
            os.system("df -h")
            print()
            input("Press enter to main menu: ")
            break
        elif(a==4):
            dirname=input("Enter the name of mounting directory: ")
            os.system("mkdir /{}".format(dirname))
            vgname=input("Enter the vgname: ")
            lvmname=input("Enter the LVMname: ")
            state=input("New lvm storage then press yes else no :")
            if(state=="yes"):
                os.system("fdisk /dev/{}/{}".format(vgname,lvmname))
                os.system("fdisk -l")
                dire=input("enter the directory: ")
                os.system("mkfs.ext4 {}".format(dire))

            os.system("mount /dev/{}/{} /{}".format(vgname,lvmname,dirname))
            print("successfully mounted")
            os.system("df -h")
            print()
            input("press enter to main menu: ")
            break
        elif(a==5):
            os.system("df -h")
            input("press enter to continue")
            break
        elif(a==6):
            os.system("vgdisplay")
            input("press enter to continue")
            break
        elif(a==7):
            os.system("lvdisplay")
            input("press enter to continue")
            break
        elif(a==8):
            os.system("fdisk -l")
            input("press enter to continue")
            break
        elif(a==9):
            exit=False
            break


