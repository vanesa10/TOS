import csv
with open('data.csv') as f:
  reader = csv.reader(f)
  r = 0
  print("Negara Hitung Jumlah Rata-rata Maks Min")
  for row in reader:
    if r > 4:
      hitung = 0
      jumlah = 0
      max = 0
      min = 0
      name = ""
      c = 0
      for col in row:
	if c == 1:
	  name = col
	elif c > 3:
	  if not col == '':
            hitung+=1
            val = float(col)
            jumlah+=val
	    if hitung == 1:
	      max = val
	      min = val
	    else:
              if val > max:
                max = val
              if val < min:
                min = val			
        c+=1	
      avg = 0
      if hitung > 0:
        avg = float(jumlah/hitung)
      else:
	avg = "-nan"
	max = "-nan"
	min = "-nan"
      print name, hitung, jumlah, avg, max, min
    r+=1
