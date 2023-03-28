# Murreviikko / Dialect week
# Dialectologically annotated and normalized dataset of dialectal Finnish tweets

Murreviikko (literally 'Dialect week') is a campaign founded in the University of Eastern Finland to promote the use of Finnish dialects in social media. It started in 2020 and takes place mid-October.

The original data was collected from Twitter with the search word murreviikko ('dialect week') and hashtag #murreviikko separately for 2020, 2021 and 2022. The current dataset combines all the original collections.

The original tweets are normalized to a phonetic standard, but word order is not altered, or grammar rules of standard Finnish followed otherwise. This means that for instance standard Finnish possessive suffixes (minun kirja-ni) are not added if they are not present in the original tweet (minun kirja). Likewise, dialect words are not corrected to the standard alternative, even if such words would exist (pruukata > pruukata instead of standard tavata).

Some policies on special cases:
- Emojis and url's are substituted with tags [emoji] and [url] in normalized text. On the original and normalized side the user-tags are substituted with @user. Hashtags are left as they are, or normalized if they contain dialectal features.
- If there is a one-to-many correspondence, the separate words are connected with an underscore (tiäksää > tiedätkö_sinä)
- Case governance follows the original tweet (me mennään > me mennään, hyö männööt > he menevät)
- Possessive suffix is added if it appears in the original: mun kodissa > minun kodissa, yksinänj > yksinäni
- Dialect words might be changed phonetically and morphologically to follow the standard (krämpkonttissi > krämppikonttisia) but not substituted with an alternative word (heikkojalkaisia).
- Some words of Swedish origin with a consonant cluster in the beginning of the word can have two possible spellings in Finnish. We opt to use a double consonant in the beginning of the word: ruukata > pruukata.
	- Please note that the two previous rules can make tweets using Helsinki slang look very distant from the standard
	- "Stadilainen voi käydä skugessa tsiigaamassa heinähattuja mutta bamlaa niin kuin aikaisemminkin."
- To remain consistent, some accepted spellings of the standard have been unified to one form:
	- muitten > muiden
	- poikain > poikien
	- ettei > että_ei

# Murreviikko

Murreviikko on Itä-Suomen yliopistossa aloitettu kampanja, jonka tavoitteena on saada ihmiset käyttämään suomen murteita sosiaalisessa mediassa. Murreviikko alkoi vuonna 2020 ja se järjestetään yleensä lokakuussa.

Alkuperäinen aineisto on kerätty Twitterin API:n avulla hakusanalla murreviikko ja tunnisteella #murreviikko erikseen vuosilta 2020, 2021 ja 2022. Nykyinen aineisto yhdistää kaikkien vuosien twiitit.

Tavoitteena on ollut normalisoida twiitit niin, että muoto- ja äänneopilliset seikat noudattavat suomen oikeinkirjoitusta. Sen sijaan esimerkiksi sanajärjestystä ei ole muutettu tai lauseopillisia muutoksia tehty. Tämä tarkoittaa sitä, että esimerkiksi possessiivisuffikseja (minun kirja-ni) ei ole lisätty, jos niitä ei ole alkuperäisessä twiitissä. Vastaavasti murteellisia sanoja ei ole käännetty yleiskieleen, vaikka niille olisi olemassa selkeä vastine (pruukata > pruukata eikä tavata).

Joitakin linjauksia koskien muoto- ja äänneopillista normalisointia:
- Emojit korvataan normalisoidussa tekstissä tunnisteella [emoji] ja linkit tunnisteella [url]. Molemmilla tasoilla käyttäjäviitteet on korvattu merkinnällä @user. Tunnisteet on jätetty sikseen tai normalisoitu, jos niissä on murreainesta.	
- Jos twiitissä olevaa sanaa vastaa useampia sana normalisoidussa tekstissä, nämä yhdistetään alaviivalla (tiäksää > tiedätkö_sinä)
- Rektio noudattaa alkuperäistä twiittiä (me mennään > me mennään, hyö männööt > he menevät)
- Possessiivisuffiksi noudattaa alkuperäistä twiittiä: (mun kodissa > minun kodissa, yksinänj > yksinäni)
- Murresanat muokataan äänne- ja muoto-opillisilta piirteiltään yleiskieltä vastaaviksi (krämpkonttissi > krämppikonttisia) mutta ei muuteta koko sanaa (heikkojalkaisia)
- Alkuperältään ruotsalaisten lainasanojen kirjoitusasussa linjana on kaksoiskonsonantti sanan alussa (ruukata > pruukata)
	- huomaa, että erityisesti slangimatkimuksissa kaksi edellistä sääntöä aiheuttavat sen, että "normalisoitu" asu voi olla hyvinkin slangimaista:
	- "Stadilainen voi käydä skugessa tsiigaamassa heinähattuja mutta bamlaa niin_kuin aikaisemminkin."
- Yleiskielessäkin hyväksyttyjä kirjoitustapoja on voitu muuttaa yhtenäisyyden nimissä: 
	- muitten > muiden
	- poikain > poikien
	- ettei > että_ei
