


i = Item(name_item = 'Samsung',price ='1000')
i_2 = Item(name_item = 'Sony',price ='900')
i_3 = Item(name_item ='Iphone', price ='1200')
i_4 = Item(name_item ='Xiaomi', price ='600')
i_5 = Item(name_item ='Huawei', price ='800')
i_6 = Item(name_item ='Redmi', price ='500')
i_7 = Item(name_item ='Yandex', price ='300')
i_8 = Item(name_item ='Pocophone', price ='450')
i_9 = Item(name_item ='Google', price ='700')
i_10 = Item(name_item ='Nokia', price ='100')


p = Purchase(name = 'Arsen', age = '21' ,item = i , date_purchase = timezone.now())
purchases_2 = Purchase(name = 'Argen', age = '18' ,item = i_2 , date_purchase = timezone.now())
purchases_3 = Purchase(name = 'Mirlan', age = '23' ,item = i_2 , date_purchase = timezone.now())
purchases_4 = Purchase(name = 'Davles', age = '25' ,item = i , date_purchase = timezone.now())
purchases_5 = Purchase.objects.create(name = 'Beka', age = '28' ,item = i_3 , date_purchase = timezone.now())
purchases_6 = Purchase.objects.create(name = 'Sultan', age = '16' ,item = i_5 , date_purchase = timezone.now())
purchases_7 = Purchase(name = 'Alym', age = '30' ,item = i_7 , date_purchase = timezone.now())
purchases_8 = Purchase(name = 'Aisultan', age = '21' ,item = i , date_purchase = timezone.now())
purchases_9 = Purchase(name = 'Bektur', age = '19' ,item = i_6 , date_purchase = timezone.now())
purchases_10 = Purchase(name = 'Aisuluu', age = '32' ,item = i_7 , date_purchase = timezone.now())
purchases_11 = Purchase(name = 'Nuriza', age = '41' ,item = i_4 , date_purchase = timezone.now())
purchases_12 = Purchase(name = 'Nuridin', age = '25' ,item = i_3 , date_purchase = timezone.now())
purchases_13 = Purchase(name = 'Syimyk', age = '22' ,item = i_8 , date_purchase = timezone.now())
purchases_14 = Purchase(name = 'Nurgul', age = '17' ,item = i_5 , date_purchase = timezone.now())
purchases_15 = Purchase(name = 'Aziz', age = '52' ,item = i_6 , date_purchase = timezone.now())
purchases_16 = Purchase(name = 'Aziza', age = '44' ,item = i_9 , date_purchase = timezone.now())
purchases_17 = Purchase(name = 'Diana', age = '34' ,item = i_10 , date_purchase = timezone.now())
purchases_18 = Purchase(name = 'Aidana', age = '13' ,item = i_8 , date_purchase = timezone.now())
purchases_19 = Purchase(name = 'Aiturgan', age = '16' ,item = i_9 , date_purchase = timezone.now())
purchases_20 = Purchase(name = 'Akyl', age = '25' ,item = i_7 , date_purchase = timezone.now())
