# Torrent Parser

Author: Yi Luo

[![Build Status](https://travis-ci.com/woodenchalet/BitTorrentParser.svg?branch=master)](https://travis-ci.com/woodenchalet/BitTorrentParser)

A simple parser for .torrent file.

## Installation

Include `torrent_parser` within your project's libary directory, often
`/lib`.  If that does not make sense to you, simply include the `torrent_parser`
subdirectory within your application's root directory

## Usage

```python

import sys

from torrent_parser import TorrentParser

path = sys.argv[1]

parser = TorrentParser(path)

torrent = parser.output_torrent_object()

```

## Workflows via Contexts

Contexts allow you to build workflows easily,

```python
import sys

from torrent_parser import TorrentParser

path = sys.argv[1]

with TorrentParser(path) as parser:
    torrent = parser.output_torrent_object()
```

## JSON Output
With code

```python
    json_output = json.dumps(torrent, default=lambda o: o.__dict__,
                             sort_keys=True, indent=4)
    print json_output
```

```json
{
    "title": "JimmyDirtnail-TheCompleteInstrumentals",
    "size": "512 kB",
    "created_by": "ia_make_torrent",
    "creation_date": "2016-06-08 19:52:59",
    "announce_list": [
        [
            "http://bt1.archive.org:6969/announce"
        ],
        [
            "http://bt2.archive.org:6969/announce"
        ]
    ],
    "files": [
        {
            "crc_checksum": "4054c82c",
            "paths": [
                "01 - DJ Dulux - As Me Provide The Legacy.mp3"
            ],
            "size": "2.8 MB"
        },
        {
            "crc_checksum": "590e3b9d",
            "paths": [
                "01 - DJ Dulux - Hard Bright City Lights.mp3"
            ],
            "size": "6.7 MB"
        },
        {
            "crc_checksum": "c0c9c70b",
            "paths": [
                "01 - DJ Dulux - The Magnificence  Of Trance.mp3"
            ],
            "size": "5.1 MB"
        },
        {
            "crc_checksum": "f66cb5b9",
            "paths": [
                "01-DjDulux-DarkQueen2014.mp3"
            ],
            "size": "1.6 MB"
        },
        {
            "crc_checksum": "dc890ae6",
            "paths": [
                "01-DjDulux-TheTimetravlerOfDragonBlood2014.mp3"
            ],
            "size": "3.2 MB"
        },
        {
            "crc_checksum": "ef4c27c3",
            "paths": [
                "01-DjDulux-TheWizird_sLightMagicOfMecrador2014.mp3"
            ],
            "size": "2.9 MB"
        },
        {
            "crc_checksum": "872e2472",
            "paths": [
                "01-JimmyDirtnail-BocaExtrandaGanda.mp3"
            ],
            "size": "9.5 MB"
        },
        {
            "crc_checksum": "f1e86ac3",
            "paths": [
                "01-JimmyDirtnail-DevelpingOfDryInpact.mp3"
            ],
            "size": "5.2 MB"
        },
        {
            "crc_checksum": "aee9f668",
            "paths": [
                "01-JimmyDirtnail-DuluxTrax.mp3"
            ],
            "size": "4.1 MB"
        },
        {
            "crc_checksum": "ee7f8bdd",
            "paths": [
                "01-JimmyDirtnail-Showgirls.mp3"
            ],
            "size": "3.0 MB"
        },
        {
            "crc_checksum": "af004bb5",
            "paths": [
                "01-JimmyDirtnail-StillNewBeat.mp3"
            ],
            "size": "1.9 MB"
        },
        {
            "crc_checksum": "0b4bcce2",
            "paths": [
                "01-JimmyDirtnail-TheCreationOfParadise.mp3"
            ],
            "size": "7.6 MB"
        },
        {
            "crc_checksum": "138f4885",
            "paths": [
                "01-JimmyDirtnail-TheDarkLord.mp3"
            ],
            "size": "10.5 MB"
        },
        {
            "crc_checksum": "ed89a525",
            "paths": [
                "01-JimmyDirtnail-ZeroTempetureDegreez.mp3"
            ],
            "size": "3.6 MB"
        },
        {
            "crc_checksum": "073566ae",
            "paths": [
                "02 - DJ Dulux - Boyz Night Out.mp3"
            ],
            "size": "6.7 MB"
        },
        {
            "crc_checksum": "01404cf7",
            "paths": [
                "02 - DJ Dulux - Develping Of Dry Inpact part II.mp3"
            ],
            "size": "10.1 MB"
        },
        {
            "crc_checksum": "8cbd90de",
            "paths": [
                "02 - DJ Dulux - Moldulator Technic Wire Of A Wizerd.mp3"
            ],
            "size": "6.2 MB"
        },
        {
            "crc_checksum": "24f9a35c",
            "paths": [
                "02 - DJ Dulux - Open your soul.mp3"
            ],
            "size": "6.2 MB"
        },
        {
            "crc_checksum": "13d763c2",
            "paths": [
                "02 - DJ Dulux - Ordinary Basterd.mp3"
            ],
            "size": "3.8 MB"
        },
        {
            "crc_checksum": "091055d0",
            "paths": [
                "02-DjDulux-ARonin_sLastSamuraiTradition2014.mp3"
            ],
            "size": "6.1 MB"
        },
        {
            "crc_checksum": "d98f3a43",
            "paths": [
                "02-DjDulux-AllMagiciensAreOpenMindedCreators2014.mp3"
            ],
            "size": "3.9 MB"
        },
        {
            "crc_checksum": "bbd91a26",
            "paths": [
                "02-DjDulux-TheOcean_sFurtuneMyraidHappiness2015.mp3"
            ],
            "size": "3.4 MB"
        },
        {
            "crc_checksum": "7a6ef10e",
            "paths": [
                "02-JimmyDirtnail-ChildOutstandinFilosofyInside.mp3"
            ],
            "size": "4.7 MB"
        },
        {
            "crc_checksum": "bb95b5ef",
            "paths": [
                "02-JimmyDirtnail-ClubChaoticPurple.mp3"
            ],
            "size": "5.3 MB"
        },
        {
            "crc_checksum": "d97abf28",
            "paths": [
                "02-JimmyDirtnail-DedicatedToConfettis.mp3"
            ],
            "size": "3.6 MB"
        },
        {
            "crc_checksum": "3be18f90",
            "paths": [
                "02-JimmyDirtnail-MultitudeVioceOfPhantasm.mp3"
            ],
            "size": "5.0 MB"
        },
        {
            "crc_checksum": "ded6265c",
            "paths": [
                "02-JimmyDirtnail-PoisonLove.mp3"
            ],
            "size": "4.9 MB"
        },
        {
            "crc_checksum": "a4028a42",
            "paths": [
                "02-JimmyDirtnail-ShadowOfTheDraught.mp3"
            ],
            "size": "1.4 MB"
        },
        {
            "crc_checksum": "86d9ed66",
            "paths": [
                "02-JimmyDirtnail-TheFlipRabbitWorld.mp3"
            ],
            "size": "5.7 MB"
        },
        {
            "crc_checksum": "af911b6a",
            "paths": [
                "02-JimmyDirtnail-Tranxzipolmatrenible.mp3"
            ],
            "size": "3.7 MB"
        },
        {
            "crc_checksum": "3f9cb9dd",
            "paths": [
                "03 - DJ Dulux - City View Across The Empire Of A Playa_z Dream.mp3"
            ],
            "size": "5.1 MB"
        },
        {
            "crc_checksum": "03de9dcd",
            "paths": [
                "03 - DJ Dulux - Dark Castle.mp3"
            ],
            "size": "6.5 MB"
        },
        {
            "crc_checksum": "45edc520",
            "paths": [
                "03 - DJ Dulux - Science Fiction Infection Of A G.mp3"
            ],
            "size": "6.8 MB"
        },
        {
            "crc_checksum": "fbf99efc",
            "paths": [
                "03 - DJ Dulux - Street Essamble Nightlife.mp3"
            ],
            "size": "8.4 MB"
        },
        {
            "crc_checksum": "fec73857",
            "paths": [
                "03 - DJ Dulux - Yadulsxiqusation.mp3"
            ],
            "size": "5.2 MB"
        },
        {
            "crc_checksum": "9aa0fa96",
            "paths": [
                "03-DjDulux-MetadorDeJoyaParaToroClase2014.mp3"
            ],
            "size": "3.2 MB"
        },
        {
            "crc_checksum": "dba9fc75",
            "paths": [
                "03-DjDulux-TheDarkBeautyOfTheButterflySignals.mp3"
            ],
            "size": "7.0 MB"
        },
        {
            "crc_checksum": "e9ba8918",
            "paths": [
                "03-JimmyDirtnail-ClubNuoveu.mp3"
            ],
            "size": "7.5 MB"
        },
        {
            "crc_checksum": "bee63567",
            "paths": [
                "03-JimmyDirtnail-DisclosyerOfAStandUpJourney.mp3"
            ],
            "size": "4.2 MB"
        },
        {
            "crc_checksum": "a15511c1",
            "paths": [
                "03-JimmyDirtnail-ExtremeTune.mp3"
            ],
            "size": "6.3 MB"
        },
        {
            "crc_checksum": "1175f4e9",
            "paths": [
                "03-JimmyDirtnail-TheDayEvilBecameOne.mp3"
            ],
            "size": "2.4 MB"
        },
        {
            "crc_checksum": "71897d76",
            "paths": [
                "03-JimmyDirtnail-TheLostNativeReturns.mp3"
            ],
            "size": "3.8 MB"
        },
        {
            "crc_checksum": "adc656f2",
            "paths": [
                "03-JimmyDirtnail-TranceExtreme.mp3"
            ],
            "size": "4.2 MB"
        },
        {
            "crc_checksum": "b36ddd93",
            "paths": [
                "04 - DJ Dulux - Crystal methed.mp3"
            ],
            "size": "5.1 MB"
        },
        {
            "crc_checksum": "1010acaa",
            "paths": [
                "04 - DJ Dulux - Hard Bright City Lights II.mp3"
            ],
            "size": "4.0 MB"
        },
        {
            "crc_checksum": "6418b75d",
            "paths": [
                "04 - DJ Dulux - Rain.mp3"
            ],
            "size": "7.3 MB"
        },
        {
            "crc_checksum": "e2186212",
            "paths": [
                "04 - DJ Dulux - Real Prostitutian Facts.mp3"
            ],
            "size": "3.9 MB"
        },
        {
            "crc_checksum": "16569c40",
            "paths": [
                "04 - DJ Dulux - Undenfined Reorginazsation Acces Denied (3).mp3"
            ],
            "size": "3.8 MB"
        },
        {
            "crc_checksum": "4208e48d",
            "paths": [
                "04 - Jimmy Michalski - Jimmy Dirtnail.mp3"
            ],
            "size": "4.6 MB"
        },
        {
            "crc_checksum": "9bfd3720",
            "paths": [
                "04-DjDulux-God_sAngerForTheLostSon_sReturn2014.mp3"
            ],
            "size": "3.7 MB"
        },
        {
            "crc_checksum": "8109cca3",
            "paths": [
                "04-DjDulux-TheSweetLobster2014.mp3"
            ],
            "size": "3.5 MB"
        },
        {
            "crc_checksum": "7169bc10",
            "paths": [
                "04-JimmyDirtnail-ClubDimensiaChemestry.mp3"
            ],
            "size": "7.3 MB"
        },
        {
            "crc_checksum": "7533d383",
            "paths": [
                "04-JimmyDirtnail-DevelpingOfDryInpactPartIi.mp3"
            ],
            "size": "9.2 MB"
        },
        {
            "crc_checksum": "33444d35",
            "paths": [
                "04-JimmyDirtnail-FusionOfMethedTranceformatic.mp3"
            ],
            "size": "5.1 MB"
        },
        {
            "crc_checksum": "a2994c4e",
            "paths": [
                "04-JimmyDirtnail-LyquidDreams.mp3"
            ],
            "size": "9.4 MB"
        },
        {
            "crc_checksum": "87cfb4cf",
            "paths": [
                "04-JimmyDirtnail-TheReturnOfXizomor.mp3"
            ],
            "size": "3.0 MB"
        },
        {
            "crc_checksum": "c1c667e1",
            "paths": [
                "04-JimmyDirtnail-Unformatztrancereformatic.mp3"
            ],
            "size": "3.4 MB"
        },
        {
            "crc_checksum": "d89f212a",
            "paths": [
                "05 - DJ Dulux - In My Distance.mp3"
            ],
            "size": "4.1 MB"
        },
        {
            "crc_checksum": "1a4072d2",
            "paths": [
                "05 - DJ Dulux - One For God And God Amoungst Us All.mp3"
            ],
            "size": "4.4 MB"
        },
        {
            "crc_checksum": "476a1a9e",
            "paths": [
                "05 - DJ Dulux - Trance Factory.mp3"
            ],
            "size": "6.5 MB"
        },
        {
            "crc_checksum": "3155ef50",
            "paths": [
                "05 - DJ Dulux - White Hard Brick Street Tigers.mp3"
            ],
            "size": "9.4 MB"
        },
        {
            "crc_checksum": "66b1d351",
            "paths": [
                "05-DjDulux-TheCordMelodyOfAChildOutstandinPhilosophy2014.mp3"
            ],
            "size": "3.5 MB"
        },
        {
            "crc_checksum": "f27e5498",
            "paths": [
                "05-DjDulux-TheForbiddenLove2014.mp3"
            ],
            "size": "3.7 MB"
        },
        {
            "crc_checksum": "61decadc",
            "paths": [
                "05-JimmyDirtnail-NoRialityVisionInsideOfMe.mp3"
            ],
            "size": "4.3 MB"
        },
        {
            "crc_checksum": "8c7af8f5",
            "paths": [
                "05-JimmyDirtnail-TheFlipRabbit.mp3"
            ],
            "size": "7.5 MB"
        },
        {
            "crc_checksum": "d57ad344",
            "paths": [
                "05-JimmyDirtnail-TheImageInMyMind.mp3"
            ],
            "size": "6.0 MB"
        },
        {
            "crc_checksum": "aba0bb9e",
            "paths": [
                "05-JimmyDirtnail-TheMagnificenceOfTrance.mp3"
            ],
            "size": "4.9 MB"
        },
        {
            "crc_checksum": "2c1e2038",
            "paths": [
                "05-JimmyDirtnail-Zulumiflex.mp3"
            ],
            "size": "5.1 MB"
        },
        {
            "crc_checksum": "797fd9af",
            "paths": [
                "06 - DJ Dulux - Conference Of Night Peaple.mp3"
            ],
            "size": "6.6 MB"
        },
        {
            "crc_checksum": "84b9f25e",
            "paths": [
                "06 - DJ Dulux - Intoxacation.mp3"
            ],
            "size": "5.5 MB"
        },
        {
            "crc_checksum": "5aeecc10",
            "paths": [
                "06 - DJ Dulux - My Dark Art (2).mp3"
            ],
            "size": "1.8 MB"
        },
        {
            "crc_checksum": "40aff49c",
            "paths": [
                "06 - DJ Dulux - Short Circuit.mp3"
            ],
            "size": "4.6 MB"
        },
        {
            "crc_checksum": "8f576764",
            "paths": [
                "06-JimmyDirtnail-FixThatUp.mp3"
            ],
            "size": "6.7 MB"
        },
        {
            "crc_checksum": "92af260b",
            "paths": [
                "06-JimmyDirtnail-HolocoastOfPurpleSkyOfDreams.mp3"
            ],
            "size": "7.9 MB"
        },
        {
            "crc_checksum": "7089eae6",
            "paths": [
                "06-JimmyDirtnail-NoTresspasenOnHolyGround.mp3"
            ],
            "size": "3.5 MB"
        },
        {
            "crc_checksum": "653e982a",
            "paths": [
                "06-JimmyDirtnail-Trembelince.mp3"
            ],
            "size": "3.6 MB"
        },
        {
            "crc_checksum": "b932b329",
            "paths": [
                "07 - DJ Dulux - A World War Cold Last Empire.mp3"
            ],
            "size": "5.7 MB"
        },
        {
            "crc_checksum": "f026cf33",
            "paths": [
                "07 - DJ Dulux - Deep Trouble On The Corner 1989.mp3"
            ],
            "size": "6.8 MB"
        },
        {
            "crc_checksum": "e4813ef9",
            "paths": [
                "07 - DJ Dulux - Disclosyer Of A Stand Up Journey.mp3"
            ],
            "size": "4.5 MB"
        },
        {
            "crc_checksum": "945ead3b",
            "paths": [
                "07 - DJ Dulux - Outside my sleep.mp3"
            ],
            "size": "8.1 MB"
        },
        {
            "crc_checksum": "e02450f4",
            "paths": [
                "07-JimmyDirtnail-AsMeProvideTheLegacy.mp3"
            ],
            "size": "2.7 MB"
        },
        {
            "crc_checksum": "a4f723a7",
            "paths": [
                "07-JimmyDirtnail-EternalCrystalSoulz.mp3"
            ],
            "size": "3.1 MB"
        },
        {
            "crc_checksum": "afb14e21",
            "paths": [
                "08 - DJ Dulux - Fix That Up.mp3"
            ],
            "size": "7.0 MB"
        },
        {
            "crc_checksum": "d0c450b6",
            "paths": [
                "08 - DJ Dulux - Poisen love.mp3"
            ],
            "size": "7.4 MB"
        },
        {
            "crc_checksum": "1c493db4",
            "paths": [
                "08 - DJ Dulux - The illuision Of A City Ullitstrator.mp3"
            ],
            "size": "4.3 MB"
        },
        {
            "crc_checksum": "4c2cab8a",
            "paths": [
                "08 - DJ Dulux - Universal Mind Of A Dream As One.mp3"
            ],
            "size": "4.3 MB"
        },
        {
            "crc_checksum": "89ab46b5",
            "paths": [
                "08-JimmyDirtnail-IceDealer.mp3"
            ],
            "size": "3.8 MB"
        },
        {
            "crc_checksum": "a6b05baa",
            "paths": [
                "08-JimmyDirtnail-Infoxcretiblewizerd.mp3"
            ],
            "size": "3.1 MB"
        },
        {
            "crc_checksum": "07b052b8",
            "paths": [
                "09 - DJ Dulux - Late Night Vibe.mp3"
            ],
            "size": "5.9 MB"
        },
        {
            "crc_checksum": "fbf3e234",
            "paths": [
                "09 - DJ Dulux - Mony Crystal.mp3"
            ],
            "size": "6.7 MB"
        },
        {
            "crc_checksum": "ce6b5ec0",
            "paths": [
                "09 - DJ Dulux - Rythem Of The Night.mp3"
            ],
            "size": "7.0 MB"
        },
        {
            "crc_checksum": "f157b5f4",
            "paths": [
                "09 - DJ Dulux - The Poet.mp3"
            ],
            "size": "10.8 MB"
        },
        {
            "crc_checksum": "3b36ddd5",
            "paths": [
                "09-JimmyDirtnail-FeelinOnMe.mp3"
            ],
            "size": "4.2 MB"
        },
        {
            "crc_checksum": "1e6d3c17",
            "paths": [
                "10 - DJ Dulux - 76 grams.mp3"
            ],
            "size": "11.0 MB"
        },
        {
            "crc_checksum": "93d5e79d",
            "paths": [
                "10 - DJ Dulux - In Party Out Drugs Exit.mp3"
            ],
            "size": "5.7 MB"
        },
        {
            "crc_checksum": "70a81daf",
            "paths": [
                "10 - DJ Dulux - Miami Flava.mp3"
            ],
            "size": "1.9 MB"
        },
        {
            "crc_checksum": "6cfeb26f",
            "paths": [
                "10 - DJ Dulux - Multitude Vioce Of Phantasm.mp3"
            ],
            "size": "6.6 MB"
        },
        {
            "crc_checksum": "529cff2b",
            "paths": [
                "10-JimmyDirtnail-Trippin.mp3"
            ],
            "size": "5.2 MB"
        },
        {
            "crc_checksum": "45d47b20",
            "paths": [
                "11 - DJ Dulux - The Killa _ The Dopedealer.mp3"
            ],
            "size": "4.7 MB"
        },
        {
            "crc_checksum": "963daecb",
            "paths": [
                "13 - DJ Dulux - Frozin.mp3"
            ],
            "size": "5.1 MB"
        },
        {
            "crc_checksum": "7383fb06",
            "paths": [
                "14 - DJ Dulux - Increase The Fear.mp3"
            ],
            "size": "3.7 MB"
        },
        {
            "crc_checksum": "ba6af1bd",
            "paths": [
                "15 - DJ Dulux - Lyquid Gangsta Stratosfeer.mp3"
            ],
            "size": "4.4 MB"
        },
        {
            "crc_checksum": "2fd7e41b",
            "paths": [
                "2 G'z 4 In Tha Back Rollin Like A Mack(prod by jimmy michalski).MP3"
            ],
            "size": "3.9 MB"
        },
        {
            "crc_checksum": "36c92cb6",
            "paths": [
                "600 Degreez(prod by jimmy michalski).MP3"
            ],
            "size": "4.5 MB"
        },
        {
            "crc_checksum": "a0af4d4d",
            "paths": [
                "AfricanWoman.mp3"
            ],
            "size": "4.5 MB"
        },
        {
            "crc_checksum": "ae72e6cb",
            "paths": [
                "AliceInWonderland.mp3"
            ],
            "size": "3.7 MB"
        },
        {
            "crc_checksum": "86fe7665",
            "paths": [
                "Allah The Fergiving One(prod by jimmy michalski)2015.MP3"
            ],
            "size": "3.1 MB"
        },
        {
            "crc_checksum": "35197bae",
            "paths": [
                "Almost Out Tha Game.MP3"
            ],
            "size": "3.1 MB"
        },
        {
            "crc_checksum": "69e0eaa5",
            "paths": [
                "Angels&Demons(prod by jimmy michalski).WAV"
            ],
            "size": "5.9 MB"
        },
        {
            "crc_checksum": "886b41d9",
            "paths": [
                "Anville (prod by jimmy michalski)2014.MP3"
            ],
            "size": "3.8 MB"
        },
        {
            "crc_checksum": "51200e6e",
            "paths": [
                "Arabic Truses.MP3"
            ],
            "size": "2.9 MB"
        },
        {
            "crc_checksum": "7f086c85",
            "paths": [
                "ArabicMultitudeVioceOfPhantasm.mp3"
            ],
            "size": "4.6 MB"
        },
        {
            "crc_checksum": "3c189e7e",
            "paths": [
                "AxtradFiluxiquDoxuriousproducedDoorJimmyMichalski2014.mp3"
            ],
            "size": "3.8 MB"
        },
        {
            "crc_checksum": "b387e9c9",
            "paths": [
                "Beast Of The East(prod by jimmy michalski).MP3"
            ],
            "size": "2.0 MB"
        },
        {
            "crc_checksum": "3d4f29b2",
            "paths": [
                "JimmyDirtnail-TheCompleteInstrumentals_meta.sqlite"
            ],
            "size": "258 kB"
        },
        {
            "crc_checksum": "d7fb507f",
            "paths": [
                "JimmyDirtnail-TheCompleteInstrumentals_meta.xml"
            ],
            "size": "1 kB"
        },
        {
            "crc_checksum": "78c5e22d",
            "paths": [
                "afro gangsta american trible gang(prod by jimmy michalski).MP3"
            ],
            "size": "3.4 MB"
        },
        {
            "crc_checksum": "d968c123",
            "paths": [
                "bells rythem crasher.MP3"
            ],
            "size": "3.0 MB"
        },
        {
            "crc_checksum": "7eca33e6",
            "paths": [
                "belly.MP3"
            ],
            "size": "3.8 MB"
        }
    ]
}
```