pagina=open("trabalho.html","w")
pagina.write("""
<html lang=\"pt-BR\">
<head>
<title>Saúde mental na Pandemia</title>
</head>
<body>
<p>Os dados obtidos foram:</p>
""")
#Respostas

resp = [9, 3, 7, 0, 6, 5, 8, 4, 7, 4, 10, 8, 3, 10, 1, 10, 9, 4, 8, 7, 3, 2, 0, 1]
pagina.write("<p>Respostas:%s</p>\n" %resp)
respord = sorted(resp)
pagina.write("<p>A ordenação da lista:%s</p>\n" %respord)
#Determinar menor nota, maior nota, amplitude e a média das respostas
i = min(resp)
j = max(resp)
k = (max(resp) - min(resp))
l = (sum(resp)/len(resp))
pagina.write("<p>Menor nota:%d</p>\n" % i)
pagina.write("<p>Maior nota:%d</p>\n" % j)
pagina.write("<p>Amplitude das notas:%d</p>\n" % k)
pagina.write("<p>Média das notas:%d</p>\n" % l)
pagina.write("<p>==============================</p>\n")
for x in range (0, 10+1):
  y = ("Número de pessoas que deram notas {} : {}".format (x, resp.count(x)))
  pagina.write("<p>%s</p>\n" %y)

pagina.write("""
<p>==============================</p>
</body>
</html>
""")
pagina.close()
