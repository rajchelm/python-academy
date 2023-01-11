
data = True
if data == True:
    print("data jest true")

if data is True:    #test czy data oraz true wskazują na ten sam obiekt, bardzo wolne
    print("data is true")

if data:            #preferowany sposób, który sprawdza zcy data jest true
    print("data jest true")


data = False

if data != True:    #jeśli data nie jest równe True - działa ale nie jest rekomendowane
    print("data != true")
if data is not True:# podobnie działa ale bardzo wolne i nierekomendowane
    print("data is not True")
if not data:        #preferowany sposób który sprawdza czy data jest False
    print("data is not true")
