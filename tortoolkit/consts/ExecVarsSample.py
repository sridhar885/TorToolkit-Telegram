try:
    from .ExecVars import ExecVars
except:
    class ExecVars:
        # Set true if its VPS
        IS_VPS = False
        
        API_HASH = "89ebdbc6e7bf9195bde696b0e9b3c387"
        API_ID = 8941261
        BOT_TOKEN = "1973792558:AAGvJ_kdA8n7wfqoTDYR83XNYdKrC9wNy50"
        BASE_URL_OF_BOT = "http://20.96.123.67"

        # Edit the server port if you want to keep it default though.
        SERVPORT = 80

        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [-1001508551596]
        OWNER_ID = 2025727672
        
        # Google Drive Index Link should include the base dir also See readme for more info
        GD_INDEX_URL = True

        # Time to wait before edit message
        EDIT_SLEEP_SECS = 10

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 170000000000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress 
        COMPLETED_STR = "▰"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "▱"

        # DB URI for access
        #  DB_URI = "postgres://ihxrvqrj:5e-1d57pAhNUxMLE0bKEqeAIRNVDYVxx@kashin.db.elephantsql.com/ihxrvqrj"
        
        # UNCOMMENT THE BELOW LINE WHEN USING CONTAINER AND COMMENT THE UPPER LINE
        DB_URI = "dbname=tortk user=postgres password=your-pass host=127.0.0.1 port=5432"
        
        # MEGA CONFIG
        MEGA_ENABLE = True
        MEGA_API = "o5EmgDSK"
        MEGA_UNAME = None
        MEGA_PASS = None

        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = "/"

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = False

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = False
        
        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = "onedrive"

        # Max size of a playlist that is allowed (Number of videos)
        MAX_YTPLAYLIST_SIZE = 2000
        
        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 10000

        # Set this to your bot username if you want to add the username of your bot at the end of the commands like
        # /leech@TorToolkitBot so the value will be @TorToolkitBot
        BOT_CMD_POSTFIX = "@megaheda" 

        # Time out for the status Delete.
        STATUS_DEL_TOUT = 10

        # Allow the user settings to be accessed in private
        USETTINGS_IN_PRIVATE = True

        # Torrent max time to collect metadata in seconds
        TOR_MAX_TOUT = 180

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50,10,2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        EXPRESS_UPLOAD = True
        





