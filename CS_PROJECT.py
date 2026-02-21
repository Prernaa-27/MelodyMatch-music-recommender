# ==========================================================================================================================================
# Importing MYSQL module:
import mysql.connector as MSQL

# Establishing connection:
# cor.execute('create database "MUSIC_SELECTOR"')
con = MSQL.connect(
    host="localhost", user="root", password="pb_bmu_27", database="music_selector"
)
print(
    "------------------------------------------------------------------------------------------------------------------"
)
print(
    "|!!!!!!!-------------- WELCOME TO MelodyMatch --------------!!!!!!!|".center(115)
)
print(
    "------------------------------------------------------------------------------------------------------------------"
)

if con.is_connected():
    print("CONNECTION ESTABLISHED!")

print("\n")
print(
    "------------------------------------------------------------------------------------------------------------------"
)

cor = con.cursor()
# ==========================================================================================================================================


# Creating schemas:

##cor.execute("""
##
##    CREATE TABLE tracks(
##    ID INTEGER PRIMARY KEY,
##    TITLE VARCHAR(225),
##    PRODUCED_BY VARCHAR(225),
##    LANG_ID INTEGER,
##    MOOD_ID INTEGER,
##    ERA_ID INTEGER
##    );
##
##""")
##print('DONE')


##cor.execute("""
##
##    CREATE TABLE directory(
##    ID INTEGER PRIMARY KEY,
##    TITLE VARCHAR(225),
##    PRODUCED_BY VARCHAR(225),
##    LANG VARCHAR(225),
##    MOOD VARCHAR(225),
##    ERA VARCHAR(225)
##    );
##
##""")
##print('DONE')


# ==========================================================================================================================================
# PROVIDING CHOICE TO THE USER:
choice = input(
    """1---->FIND MUSIC
2---->MAKE YOUR OWN DIRECTORY
ENTER YOUR CHOICE: """
)
if choice == "1":
    # INSERTING VALUES IN TABLE-->'tracks':
    # TRACKS FOR ERA 1900's:
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (1,"Sandese Aate Hai","Roop Kumar Rathod and Sonu Nigam","1","7","1")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (2,"Chaiyya Chaiyya","Sukhwinder Singh & Sapna Awasthi","1","8","1")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (3,"Mera Piya Ghar Aaya","Kavita Krishnamurthy","1","1","1")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (4,"Hindustani","Udit Narayan","1","7","1")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (5,"Zara Sa Jhoom Loon Main","Abhijeet Bhattacharya & Asha Bhosle","1","8","1")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (6,"My Heart Will Go On","Celine Dion","2","2","1")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (7,"No Scrubs","TLC","2","8","1")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (8,"Bitter Sweet Symphony","The Verve","2","6","1")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (9,"One In A Million","Bosson","2","8","1")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (10,"Long Way To Go","Cassie","2","3","1")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (11,"Mera Laung Gawacha","Musarrat Nazir","3","1","1")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (12,"Dil Da Mamla Hai","Gurdas Maan","3","4","1")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (13,"Kala Shah Kala","Anamika","3","3","1")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (14,"Billo Ni Tera Lal Ghagra","Malkit Singh","3","3","1")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (15,"Dil Luteya","Jazzy B and Apache Indian","3","8","1")'
    )
    # TRACKS FOR ERA 2000's:
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (16,"Koi Kahe Kehta Rahe","Shankar Mahadevan and Kavita Krishnamurthy","1","8","2")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (17,"Maa Tujhe Salaam","A.R. Rahman","1","7","2")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (18,"Mitwa","KShafqat Amanat Ali","1","5","2")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (19,"Koi Mil Gaya","Udit Narayan and Kavita Krishnamurthy","1","8","2")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (20,"Bole Chudiyan","Amit Kumar, Udit Narayan, Alka Yagnik, Sonu Nigam, Kavita Krishnamurthy, and Kareena","1","1","2")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (21,"Mr. Brightside"," The Killers","2","3","2")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (22,"Beautiful","Christina Aguilera","2","3","2")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (23,"Irreplaceable","Beyoncé","2","4","2")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (24,"I Gotta Feeling","The Black Eyed Peas","2","1","2")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (25,"Chasing Cars","Snow Patrol","2","4","2")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (26,"Maiyya Yashoda","Alka Yagnik, Anuradha Paudwal, Kavita Krishnamurthy","3","8","2")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (27,"Nach Baliye","Stereo Nation","3","3","2")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (28,"Dil Luteya","Jazzy B, Apache Indian","3","1","2")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (29,"Jind Mahi","Malkit Singh","3","1","2")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (30,"Gabru","Honey Singh","3","4","2")'
    )
    # TRACKS FOR ERA 2010's:
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (31,"Dheere Dheere","Honey Singh","1","3","3")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (32,"Gallan Goodiyaan","Yashita Sharma, Manish Kumar Tipu, Farhan Akhtar, Shankar Mahadevan, Sukhwinder Singh","1","1","3")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (33,"Balam Pichkari","Vishal Dadlani, Shalmali Kholgade","1","8","3")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (34,"Hindustani","Udit Narayan","1","7","3")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (35,"Kala Chashma","Amar Arshi, Badshah, Neha Kakkar","1","8","3")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (36,"Believer","Imagine Dragons","2","3","3")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (37,"Shape of You","Ed Sheeran","2","3","3")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (38,"Faded","Alan Walker","2","8","3")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (39,"Shake It Off","Taylor Swift","2","8","3")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (40,"Havana","Camila Cabello ft. Young Thug","2","3","3")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (41,"Angreji Beat","Honey Singh, Gippy Grewal","3","8","3")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (42,"High Heels","Honey Singh, Jaz Dhami","3","3","3")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (43,"Suit Suit","Guru Randhawa, Arjun","3","8","3")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (44,"BLak 28 Kudi Da","Diljit Dosanjh, Yo Yo Honey Singh","3","4","3")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (45,"Swag Mera Desi","Raftaar","3","3","3")'
    )
    # TRACKS FOR TRENDING SONGS:
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (46,"Chaleya","Arijit Singh and Shilpa Rao","1","1","4")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (47,"What Jhumka ?"," Arijit Singh, Jonita Gandhi, Pritam Chakraborty, Amitabh Bhattacharya, Ranveer Singh","1","3","4")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (48,"Kalaastar","Gill Machhrai, Rony Ajnali, and Yo Yo Honey Singh","1","8","4")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (49,"Jhoome Jo Pathaan"," Arijit Singh, Vishal Dadlani, Shekhar Ravjiani, Sukriti Kakar","1","1","4")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (50,"Maan Meri Jaan","King","1","2","4")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (51,"Dance the Night","Dua Lipa","2","1","4")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (52,"Cupid","Bryson Bernard","2","1","4")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (53,"Cruel Summer","Tylor Swift","2","4","4")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (54,"Different Kind Of Beautiful","Alec Benjamin","2","1","4")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (55,"What Was I Made For?","Billie Eilish","2","2","4")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (56,"With You","AP Dhillon","3","5","4")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (57,"CHEQUES","Shubh","3","4","4")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (58,"One Love","Shubh","3","10","4")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (59,"Hass Hass","Diljit Dosanjh","3","8","4")'
    )
    cor.execute(
        'INSERT INTO tracks (id,title,produced_by,lang_id,mood_id,era_id) VALUES (60,"Softly","Karan Aujla and Ikky","3","4","4")'
    )

    # ==========================================================================================================================================

    # Taking user input:

    while True:
        continue_input = input("CONTINUE? (Y/N)").upper()
        print(
            "=================================================================================================================="
        )
        print("\n")
        if continue_input in ("Y", "YES"):
            LANG = None
            while LANG not in ("1", "2", "3"):
                LANG = input(
                    """What language should the music be in?
                1-->HINDI
                2-->ENGLISH
                3-->PUNJABI
                ----->"""
                )
                print("\n")
                print(
                    "------------------------------------------------------------------------------------------------------------------"
                )
                print("\n")

            MOOD = None
            while MOOD not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
                MOOD = input(
                    """What mood or emotion are you looking for in the music?
                1-->CELEBRATORY/POP
                2-->EMOTIONAL
                3-->ENERGETIC
                4-->HIP-HOP
                5-->SOOTHING
                6-->INSPIRATIONAL
                7-->PATRIOTIC
                8-->UPBEAT
                9-->MYSTERIOUS
                10-->SENTIMENTAL
                ----->"""
                )
                print("\n")
                print(
                    "------------------------------------------------------------------------------------------------------------------"
                )
                print("\n")

            ERA = None
            while ERA not in ("1", "2", "3", "4"):
                ERA = input(
                    """Which era does the song belong to?
                1-->90's
                2-->2000's
                3-->2010's
                4-->TRENDING
                ----->"""
                )
                print("\n")
                print(
                    "------------------------------------------------------------------------------------------------------------------"
                )
                print("\n")

            # ==========================================================================================================================================
            cor.execute(
                "SELECT title, produced_by FROM tracks WHERE lang_id={} AND mood_id={} AND era_id={}".format(
                    LANG, MOOD, ERA
                )
            )
            result = cor.fetchall()

            if not result:
                print("NO RECOMMENDATIONS FOUND >﹏< ")
            else:
                for row in result:
                    print(
                        "---------------------------------------------------------------------------------------------------------------------"
                    )
                    print(str(row))
                    print(
                        "---------------------------------------------------------------------------------------------------------------------"
                    )

        elif continue_input in ("N", "NO"):
            print(
                "=================================================================================================================="
            )
            print("THANK YOU!".center(121))
            print(
                "=================================================================================================================="
            )
            break
        else:
            print("INVALID input. Please enter Y/N.")

    con.close()

# ==========================================================================================================================================

elif choice == "2":
    option = input(
        """1---> INSERT MUSIC
2---> UPDATE
3---> DELETE
4---> EXIT
"""
    )

    if option == "1":
        while True:
            continue_input_2 = input("CONTINUE? (Y/N)").upper()
            print(
                "=================================================================================================================="
            )
            print("\n")
            if continue_input_2 in ("Y", "YES"):
                SNO = int(input("ENTER THE INDEX OF THE SONG: "))
                TITLE = input("ENTER THE TITLE OF THE SONG: ")
                COMPOSER = input("ENTER THE NAME OF THE ARTIST: ")
                LANG = input("ENTER THE LANGUAGE OF THE SONG: ")
                MOOD = input("ENTER THE MOOD/EMOTION OF THE SONG: ")
                ERA = input("ENTER THE ERA OF THE SONG: ")
                print("\n")
                print(
                    "------------------------------------------------------------------------------------------------------------------"
                )
                print("\n")

                cor.execute(
                    "INSERT INTO directory (id, title, produced_by, lang, mood, era) VALUES (%s, %s, %s, %s, %s, %s);",
                    (SNO, TITLE, COMPOSER, LANG, MOOD, ERA),
                )
                con.commit()
            else:
                break

    if option == "2":
        column = input("ENTER THE COLUMN NAME TO BE UPDATED: ")
        value = input("ENTER THE NEW VALUE: ")
        condition = input("ENTER CONDITION: ")

        try:
            cor.execute(
                "UPDATE directory SET {} = %s WHERE {};".format(column, condition),
                (value,),
            )
            con.commit()
            print("Update successful!")

        except Exception as e:
            print(f"Error: {e}")
            con.rollback()

    if option == "3":
        cor.execute("DELETE FROM directory;")
        con.commit()
        print("DONE")

    if option == "4":
        print(
            "=================================================================================================================="
        )
        print("THANK YOU!".center(121))
        print(
            "=================================================================================================================="
        )

con.close()
# -------------------------------------------------------------------------------------END OF CODE--------------------------------------------------------------------------------------#
