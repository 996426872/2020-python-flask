import wordcloud
import qrcode

ll = "One world,one python!"
cy = wordcloud.WordCloud(background_color="white")
cy.generate(ll)
cy.to_file("cy.png")

img = qrcode.make('http://python123.io')
img.save("qr.png")