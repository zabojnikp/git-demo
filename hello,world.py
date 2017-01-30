print ("hello, world")

class Kotatko:
    def zamnoukej(self, zprava):
        print("Kotatko: {}".format(zprava))

kotatko = Kotatko()
kotatko.zamnoukej("Mnaaau")

class Zajicek:
    def hopkej(self, zprava):
        print("{}: {}".format(self.jmeno, zprava))

zajicek = Zajicek()
zajicek.jmeno = "Claudio"
zajicek.hopkej("hop,hop")


jinyzajicek = Zajicek()
jinyzajicek.jmeno = "Osvald"
jinyzajicek.hopkej('nebudu, hopkat')
print("osvald je liny".capitalize())


print("ahoj".capitalize())

print ("where am I now?")
