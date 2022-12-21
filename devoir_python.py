import random

#le wap testel silvouple pkite DebuG a False, debug True a se pou mwn selman
debug=False

def lawoulet():
    print("Bonjou byenvini nan ti jwe lawoulet nou an.")
    print("Machin nan gen pou chwazi yon nomb  ant 0 ak 5000 epi ou nan ap eseye devinel")
    print("ou gen 5 tantativ")
    continu=True
    while continu:
        nomb_machin=random.randrange(0,500)
        
        essaie=5
        while True:
            if essaie==0:
                print(f'tantative ou io fini, nomb lan te {nomb_machin}')
                break
            try:
                nomb_itilizate=int(input('Entre nomb ou an sivouple \n'))
                
                if nomb_itilizate>nomb_machin:
                    print('Nomb ou antre a two gwo eseye youn ki pipiti')
                    essaie -=1
                    print(f'ou rete {essaie} tantativ')
                elif  nomb_itilizate<nomb_machin:
                    essaie -=1
                    print('nomb ou antre a two piti eseye youn ki pi gwo')
                    print(f'ou rete {essaie} tantativ')
                elif nomb_itilizate==nomb_machin:
                    print('Bravo!!!!1 ou jwenn nomb lan')
                    break
            except:
                    print('Saw antre a pa yon nomb')
        rr=input('peze 1 ou kntinye oubyn nenpot ki lot bagay pou kite jwet la')
        
        if rr == '1':
            print('ann continye!')

        else:
            
            continu==False
            break


    print('Merci a la prochaine ;) \n\n')

def test(i,condition):
    if debug:
        if condition:
            print(f'Test {i} has succed')

        else:
            print(f'Test {i} has failed')

def check(*args):
    a=input('Antre chif ou a.. \n')
    if a =='#':
        return a
    try:
        a=int(a)
        if a in args:
            return a
        else:
            return 0
    except:
        print('saw antre a pa yon chif \n')
        return 0

def devwa_12_dec_2022():
    print("Bienvini nan devwa ki te bay 12 decembre 2022 a, nan devwa sa ou ap gen chans pou run yon seri de ti porgram sou theme fonksyon.")
    
    while True:
        print('peze 1 pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon.')
        print('peze 2 pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon.')
        print('peze 3 pou Jenere yon SLUG apati chenn nan. Nan yon SLUG, tout karaktè ki akseptab yo se: alfanimerik ak "-"')
        print('peze 4 pou separe chak lèt nan yon mo ak yon vigil')
        print('peze 5 pou kripte yon mo, avèk endèks li nan alfabè a. Chak karaktè dwe separe ak yon tirè.')
        print('peze 6 pou dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a, separe ak yon tirè.')
        print('peze 7 pou pèmite valè . Answit retounen tou 2 valè yo sou fòm Tuple.')
        print('peze 8 pou retounen inisyal yon non')
        print('peze # pou retounen nan menu avan la')
        choice=check(1,2,3,4,5,6,7,8)
        if choice == '#':
            break
        
        if choice==2:
            l="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            code=""
            n=0
            while True:
                try:
                    n=int(input('antre yon chif ki pa pi plis ke 62 eki pa pi piti ke zewo' ))
                    if n in range(0,62):
                        break
                except:
                    print('saw antre a pa yon chif')

            for i in range(0,n):
                rando= random.choice(l)
                l = l.replace(rando,"")
                
                code=code+rando
            
            print(f'votre code est {code} \n\n')

        if choice == 1:
            l="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            code=""
            n=0
            while True:
                try:
                    n=int(input('antre yon chif ki pa pi plis ke 62 eki pa pi piti ke zewo: ' ))
                    if n in range(0,62):
                        break
                except:
                    print('saw antre a pa yon chif')

            for i in range(0,n):
                rando= random.choice(l)
                l = l.replace(rando,"")
                
                code=code+rando
            
            print(f'votre code est {code} \n\n')

        if choice == 3:
            a= input('antre chen karaktew la')
            l="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-"
            a=a.replace(' ','-')
            for x in a:
                if x not in l:
                    print('entrer non valid')
                    return
            print(f'Nouvo slug ou a se {a}\n\n')
        
        if choice == 4:
            a=input('antre mo ou a: ')
            for x in a:
                if x == ' ':
                    print('ou dwe rantre yon sel mot')
                    return
                d=x+','
                a=a.replace(x,d)
            print(a[:-1],'\n\n')

        if choice == 5:
            word=input('antre mow la: ')
            ch="abcdefghijklmnopqrstuvwxyz"

            code = ""

            for c in word:
                code=code+str(ch.index(c))+"-"
            
            code = code[:-1]

            print(code)
        
        if choice == 6:
            input_val=input('Entrer mow la.')
            def decrypte(input_val):
                input_val = input_val.split("-")

                l="abcdefghijklmnopqrstuvwxyz"

                ii = ""

                for i in input_val:
                    ii=ii+l[int(i)-1]

                print(ii)
            decrypte(input_val)

        if choice == 7:
            def premut(a,b):
                return(b,a)
            print(premut(input('antre premye vale a'),input('antre dezyem vale a')))

        
        if choice == 8:
            def inisyal(non):
                er = ""
                non = non.replace(" ","-")
                non = non.split("-")

                for w in non:
                    er = er + w[0].capitalize()

                print(er)
                return er
            inisyal(input('antre nonw'))      
  
def devwa_20_dec_2022():


    class _file():
        def __init__(self,path):
            self.path=path

        def read(self):
            with open(self.path,'r') as file:
                print(file.read())
                print('file read with success')

        def append(self,x):
            with open(self.path,'a') as file:
                file.write(x)
                print('content append with success')

        def write(self,x):
            with open(self.path,'w') as file:
                file.write(x)
                print('content write with success')

        def clean(self):
            with open(self.path,'w') as file:
                file.write('')
                print('file clean with success')

        def prepend(self,x):
            with open(self.path,'r') as file:
                xx=file.read()

            with open(self.path,'w') as file:
                x=x+"\n"+xx
                file.write(x)
            print('content prepend with success')

    first= _file('txt.txt')
    first.append('fadfadafd')



def list_ansyen_devwa():
    while True:
        devwa=[]
        devwa.append( [lambda: lawoulet(),lawoulet.__name__])
        devwa.append([lambda:devwa_12_dec_2022(),devwa_12_dec_2022.__name__])
        devwa.append([lambda:devwa_20_dec_2022(),devwa_20_dec_2022.__name__])
        if len(devwa) ==0:
            print('Pako gen devwa ki bay')
            return
        ee=0
        args=[]
        for x in devwa:
            print(f'peze {ee+1} pou ka run {x[1]} la')
            ee+=1
            args.append(ee)
        
        print('peze # pour retounen nan menu avan an')
        args.append('#')
        args=tuple(args)
        choice=check(*args)
        if choice == '#':
            break
        if choice != 0:
            devwa[choice-1][0]()      



def main_menu():
    keep=True
    while keep:
        print("Peze 1 pou ka we denye devwa an dat la oubyen peze 2 pou ka we tout devwa li yo oubyen peze 3 pou kite program nan.")

        choice=check(1,2,3)
        if choice==1:
            test(1,True)
            devwa_20_dec_2022()

        elif choice== 2:
            list_ansyen_devwa()
        elif choice == 3:
            test(3, True)
            keep= False

def main():
    print('Byenvini sou plateform ansanm devwa python Isai Jean Mary...')       
    main_menu()
    print('Babay et a la prochaine.......;)')

main()