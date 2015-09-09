
# Virtualna okolja
Python okolje se lahko pohvali z enim od največjih ekosistemov razširitvenih paketov (`python packages`). Operacijska sistema Linux in OS X, nekatere že privzeto namestita. Namestijo jih lahko tudi drugi programi, ki so napisani v pythonu.

Problem se pojavi, ko želimo uporabiti različne različice istega paketa. Pri tem nam pomaga paket za virtualna okolja (`virtualenv`).

## Namestitev

Namestimo ga lahko na več različnih načinov:
* Vsi sistemi: `pip install virtualenv`
* Debian/Ubuntu: `sudo apt-get install python-virtualenv`

V primeru, da `pip` še ni nameščen, ga namestimo s:
 * Debian/Ubuntu: `sudo apt-get install python-pip`
* Vsi sistemi: prenesite datoteko: [https://bootstrap.pypa.io/get-pip.py][1]in jo poženite: `python get-pip.py`

Po namestitvi `virtualenv` moramo ponovno zagnati konzolo. Preverimo, če deluje:

	$ virtualenv --version
	1.11.6

## Uporaba

`virtualenv` postavi za vsako okolje, posebno različico python interpreterja. Ta upošteva samo pakete, ki so nameščeni znotraj tega paketa.

Ustvarimo nov projekt:
	$ mkdir projekt
	$ cd projekt
	$ virtualenv ENV
	New python executable in ENV/bin/python2.7
	Also creating executable in ENV/bin/python
	Installing setuptools, pip...done.

`virtualenv` aktiviramo z ukazom:

Linux in OS X:
	projekt$  source ENV/bin/activate
	projekt$ (ENV)    
Windows[^1]:
	ENV\Scripts\activate

Aktivno virtualno okolje se izpiše v oklepaju na začetku ukazne vrstice.

Izklopimo ga z: `deactivate`

## Paketi in distribucija okolja

V aktiviran `virtualenv` namestimo pakete s programom `pip`:
	$ pip install requests
	Downloading/unpacking requests
	  Downloading requests-2.7.0-py2.py3-none-any.whl (470kB): 470kB downloaded
	Installing collected packages: requests
	Successfully installed requests
	Cleaning up...
	

Nameščene pakete vidimo z ukazom `pip freeze`:
	$ pip freeze
	requests==2.7.0
	wsgiref==0.1.2

Navada je, da seznam nameščenih paketov stranimo v datoteko `requirements.txt`. Razvijalci, ki bodo želeli uporabiti naš paket jih bodo morali samo namestit v svoje virtualno okolje:
	$ pip install -r requirements.txt

Virtualna okolja ne vidijo v paketov, ki so nameščeni v sistemski python. To pomeni, da moramo v vsako virtualno okolje namestiti vse paketke, ki jih naša aplikacija potrebuje. Porabimo sicer več prostora na disku, vendar se izognemo težavam, ki pridejo s tem, da nimamo polnega nadzora nad različicami paketov.

## Uporaba virtualenv v zunanjih procesih

Povezava z zunanji programi kot je npr. `cron` pogosto zahteva samo en ukaz. Kot smo omenili zgoraj, `virtualenv` pripravi posebno različico python interpreterja, ki ga lahko neposredno pokličemo.

	$ /home/uporabnik/projekt/ENV/bin/python /home/uporabnik/projekt/program.py

## Napredni razvoj z Virtualenvwrapper

Na računalniku, kjer razvijamo je pogosto nadležno tipkati aktivacijske ukaze. S paketom `virtualenvwrapper`[^2]dobimo dodatne ukaze v naši ukazni vrstici.

Virtualno okolje v tem primeru ustvarimo `mkvirtualenv` in vklopimo z `workon ime_okolja`. Z nekaj dodatnih razširitev pa lahko dosežemo, da se okolje aktivira takoj, ko zamenjamo trenutni direktorij.

Konfiguracija Virtualenvwrapper okolja je že izven obsega tega tečaj, ima pa domača stran obširna navodila.

[^1]:	Powershell uporabniki bodo morali prvič vklopiti dodatna dovoljenja: [https://virtualenv.pypa.io/en/latest/userguide.html][2]

[^2]:	[https://virtualenvwrapper.readthedocs.org/en/latest/][3]

[1]:	https://bootstrap.pypa.io/get-pip.py
[2]:	https://virtualenv.pypa.io/en/latest/userguide.html
[3]:	https://virtualenvwrapper.readthedocs.org/en/latest/