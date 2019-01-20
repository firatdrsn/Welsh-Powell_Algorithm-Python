#FIRAT DURSUN 151001059 N.Ö BİLGİSAYAR MÜHENDİSLİĞİ BETİK DİLLER PROJESİ WELSH-POWELL ALGORİTMASI
class algoritma: # algoritma adında sınıf oluşturduk
	def welsh_powell(Self,graf): #welsh_powell fonksiyonumuz graf isimli parametre alıyor
		renkler=["yeşil","kırmızı","sarı","mavi","siyah","turuncu","pembe","mor","lacivert","beyaz"] #10 renkli renkler listesini oluşturduk (İstenirse renk sayısı artırılır.Ama 10 renk fazlasıyla ihtiyacımızı karşılar)
		dereceligraf=[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0] #Düğümlerimizin derecesiz halini tanımladık (graf boyutu değiştirilirse sonradan buranında genişletilmesi/küçültülmesi gerekir.)
		"""
		Aşağıda:
		While döngüsüyle komşuluk matrisimizi ekrana yazdırdık.
		i değişkenimiz 0 değerindedir.
		i graf boyutundan küçük olduğu sürece while döngüsü çalışır.
		Döngü içinde graf[i] satırı grafın i. satırını yazdırır.
		i 1 artırılır.
		"""
		i=0
		print("Komşuluk matrisi=")
		print("Düğümler  0  1  2  3  4  5  6  7  8  9")
		while(i<len(graf)):
			print("\t",graf[i],i,".Düğüm")
			i=i+1
		#Listemizin komşuluk matrisini while döngüsüyle ekrana yazdırıldı.
		
		"""
		Aşağıda:
		i değişkenini 0 yaptık.derece değişkenimizide 0 değeriyle tanımladık.
		komsuluk adında liste oluşturduk.
		i graf boyutundan küçük olduğu sürece while döngüsü çalışır.
		ilk while içine girildiğinde k değişkeni 0 yapılır.
		ikinci while da k değişkeni graf boyutundan küçük olduğu sürece çalışır.
		grafın diğer düğümlerle olan komşuluklarını if ile kontrol ediyoruz.Örnek:0 düğümünün 3. sırasının değeri 1 ise 3.düğümle komşuğu vardır Eğer komşuluk varsa derece değişkenini 1 artırıyoruz.
		k değişkenini bir artırarak diğer düğümle komşuluğuna bakarız.
		ikinci while tamamlandığında komsuluk listesine derece değişkenini ekledik.
		dereceligraf listemizi yukarda derecesi 0 tanımlamıştık.Bu kısımda derecesini bulduğumuz düğümün derecesini yazdık.
		derece değişkenini 0 yaptık.
		i değişkenini 1 artırarak diğer düğümün derecesini kontrol için ilk while tekrar çalışır.
		"""
		
		i=0
		derece=0
		komsuluk=[]
		while(i<len(graf)):
			k=0
			while(k<len(graf)):
				if(graf[i][k]==1):
					derece=derece+1
				k=k+1
			komsuluk.append(derece)
			dereceligraf[i][1]=derece
			derece=0
			i=i+1

		print("Düğümlerin dereceleri \n",komsuluk) # Düğümlerin dereceleri yazdırıldı
		print("Düğümler ve Dereceleri \n",dereceligraf) # Düğümler ve dereceleri yazdırıldı
		
		"""
		Aşağıda:
		i ve j değişkenini 0 yaptık.
		i graf boyutundan küçük olduğu sürece while döngüsü çalışır.
		while içinde k değişkenini sıfır yaptık.
		ikinci bir while da k değişkeni grafdan küçük olduğu sürece çalışır.
		ikinci while da dereceligraf listesinin i.elemanının derecesi k.elemanının derecesinden büyük olup olmadığını kontrol eder.
		Eğer büyükse dereceligrafın hangi düğüm olduğunu gecici2 değişkenine atar.
		büyük olan dereceligrafın düğümüne küçük olan düğümü atar.
		küçük olan düğüme ise gecici2 de bulunan düğümü atar.
		dereceligrafdan büyük olanın derecesini gecici değişkenine atar.
		büyük olan dereceligraf düğümünün derecesine küçük olanın derecesini atar.
		küçük olan düğümün derecesini gecici değişkenindeki dereceyi aktarır.
		ikinci while döndükçe k artırılır ve büyüklük kontrol edilir.
		ikinci while bitince i değişkeni bir artırılır ve ilk while tekrarlanır.
		"""
		
		i=0
		j=0
		while(i<len(graf)):
			k=0
			while(k<len(graf)):
				if(dereceligraf[i][1]>dereceligraf[k][1]):
					gecici2=dereceligraf[i][0]
					dereceligraf[i][0]=dereceligraf[k][0]
					dereceligraf[k][0]=gecici2
					gecici=dereceligraf[i][1]
					dereceligraf[i][1]=dereceligraf[k][1]
					dereceligraf[k][1]=gecici
				k=k+1
			i=i+1

		print("Düğümlerin Sıralanmış Hali \n",dereceligraf) #düğümlerin sıralanmış halleri yazdırıldı

		renkligraf=[0,""],[1,""],[2,""],[3,""],[4,""],[5,""],[6,""],[7,""],[8,""],[9,""]#renkligraf listesi oluşturuldu.İlk sırada düğüm ikinci sırada renk olacak.Renkler boş tanımlandı.

		"""
		Aşağıda:
		k,i,r,j,l,f değişkenleri sıfır yapıldı.
		j değişkeni graf boyutundan küçük olduğu sürece ilk while çalışır.
		renkligraf listesinin ilk elemanının rengi var mı kontrol edilir.Eğer renk yoksa düğüm derecesi en yüksek olan düğüm renkligrafa atanır.
		ilk düğüme renk verildiği için l değişkeni bir artırılır.
		renkligrafda ki derecesi en yüksek olan düğüme ilk renk atanır.
		i grafdan küçük oldukça ikinci while tekrarlanır.
		k grafdan küçük oldukça üçüncü while tekrarlanır.
		ilk düğümün komşusu olmayan düğümler kontrol edilir.
		eğer komluşuk yok ise ikinci şart olarak komşu olmadığı düğüme renk yok mu ona bakar.
		O şartda sağlanıyorsa sağlanan düğüme ilk rengi atar.Ve i değişkenini renklendirdiği düğüm yapar.
		Sonra renklendirdiği düğümün komşu olmadığı düğümleri kontrol eder ve ilk rengi onlarada atar.
		döngüler bitince r değişkeni bir artırılır diğer renge geçilmesi için.i=1 ve k=0 yapılır.j bir artırılır.
		Bu işlemler ilk çalıştığında çalışır ilk renk için.
		Eğer ilk düğüme renk atanmış ise else kısmı çalışır.
		f değişkeni grafdan küçük olduğu sürece ilk while çalışır.
		Ve j değerine göre düğüm kontrol edilir.Renk ataması yapılmamışsa if bloğu çalışır.
		derecesi en yüksek 2.düğüm dugum değişkenin atanır.
		renkligraf listesinden derecesi en yüksek olan grafın rengine r değişkenine bağlı olarak renk atanır.
		i ve k değişkenine bağlı iki while ile renk atanan düğüm komşusu olmayan düğümler kontrol edilir.
		komluşuk yok ise ikinci şart olarak komşusu olmayan düğüme renk yok mu kontrol edilir.
		Renk verilmemişse verilen renk bu düğümede verilir.
		Ve whilelar ile bu işlem her düğüm için kontrol edilir.
		i,f,k sıfır yapılıp j bir artırılı ve sonraki derecesi en yüksek graf için işlemler yapılır.
		
		En son renkligraf listesi return ile geri döndürülür.
		"""
		
		k=0
		i=0
		r=0
		j=0
		l=0
		f=0
		while(j<len(graf)):
			if(renkligraf[0][1]==""):
				renkligraf[0][0]=(dereceligraf[l][0])
				l=l+1
				renkligraf[0][1]=(renkler[r])
				while(i<len(graf)):
					while(k<len(graf)):
						if(graf[i][k]==0):
							if(renkligraf[k][1]==""):
								renkligraf[k][1]=(renkler[r])
								i=renkligraf[k][0]
						k=k+1
					i=i+1
				r=r+1
				i=1
				k=0
			else:
				while(f<len(graf)):
					if(renkligraf[j][1]==""):
						dugum=dereceligraf[l][0]
						l=l+1
						renkligraf[dugum][1]=(renkler[r])
						while(i<len(graf)):
							while(k<len(graf)):
								if(graf[dugum][k]==0):
									if(renkligraf[k][1]==""):
										renkligraf[k][1]=(renkler[r])
								k=k+1
							i=i+1
						r=r+1
					f=f+1
			i=0
			f=0
			k=0
			j=j+1
		return renkligraf
#----------------------------------------------------------------------
graf=[] #graf adında liste oluşturduk
#Grafımızın komşuluk matrisini aşağıda oluşturduk.
       #0  1  2  3  4  5  6  7  8  9
graf= ([0, 1, 1, 1, 1, 0, 0, 0, 0, 0]   #0
      ,[1, 0, 1, 0, 0, 0, 0, 0, 1, 0]   #1
      ,[1, 1, 0, 0, 0, 0, 0, 0, 0, 0]   #2
      ,[1, 0, 0, 0, 1, 0, 0, 0, 0, 0]   #3
      ,[1, 0, 0, 1, 0, 1, 0, 0, 0, 0]   #4
      ,[0, 0, 0, 0, 1, 0, 1, 1, 0, 0]   #5
      ,[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]   #6
      ,[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]   #7
      ,[0, 1, 0, 0, 0, 0, 0, 0, 0, 1]   #8
      ,[0, 0, 0, 0, 0, 0, 0, 0, 1, 0])  #9
alg= algoritma() #algoritma sınıfından alg isminde nesne ürettik.
print("Renklendirilmiş Graf\n",alg.welsh_powell(graf)) #Grafımızı alg nesnesindeki welsh_powell fonksiyonuna gönderdik ve dönen değeri ekrana yazdırdık.
print("\n\n 2. ve 4. düğümü komşu yaptığımız ikinci graf \n") 
#2. düğüm ile 4.düğümü birbirine komşu yaparak graf2 nin komşuluk matrisini oluşturduk.
		#0  1  2  3  4  5  6  7  8  9
graf2= ([0, 1, 1, 1, 1, 0, 0, 0, 0, 0]   #0
      ,[1, 0, 1, 0, 0, 0, 0, 0, 1, 0]   #1
      ,[1, 1, 0, 0, 1, 0, 0, 0, 0, 0]   #2
      ,[1, 0, 0, 0, 1, 0, 0, 0, 0, 0]   #3
      ,[1, 0, 1, 1, 0, 1, 0, 0, 0, 0]   #4
      ,[0, 0, 0, 0, 1, 0, 1, 1, 0, 0]   #5
      ,[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]   #6
      ,[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]   #7
      ,[0, 1, 0, 0, 0, 0, 0, 0, 0, 1]   #8
      ,[0, 0, 0, 0, 0, 0, 0, 0, 1, 0])  #9
print("Renklendirilmiş Graf2\n",alg.welsh_powell(graf2)) #Graf 2yi alg nesnesindeki welsh_powell fonksiyonuna gönderdik ve dönen değeri ekrana yazdırdık.
#Grafların temsili görünümü RenkliGraf.png dosyasında gösterilmiştir.