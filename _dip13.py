from watermarker.marker import add_mark

add_mark(file="uvce.jpeg", 
         out="watermarked",
         mark="Dodagatta Nihar", 
         size=60,
         color="#ffffff",
         opacity=0.5, 
         angle=30, 
         space=60)