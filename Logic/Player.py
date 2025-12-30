from Utils.GetLeagueByScore import LeagueUtils

class Player:

    HighID = 0
    LowID = 0
    Name = 'You'
    Token = None
    FacebookID = None
    GameCenterID = None
    Major = 0
    Minor = 0
    Build = 0
    SessionCount = 0
    PlayTimeSeconds = 0
    DaysSinceStartedPlaying = 0
    FacebookAppId = None
    ServerTime = None
    AccountCreatedDate = None
    StartupCooldownSeconds = 0
    GoogleServiceId = None
    Region = None

    HomeVillage = None

    IsInAlliance = 0 # 0=False, 1=True
    AllianceHighID = 0
    AllianceLowID = 0
    AllianceRole = 0

    ExpLevel = 10  # (0-9=Tutorial, 10-X=No Tutorial)
    ExpPoints = 0 # Default=0
    Gold = 1000000000 # Default=750
    Elixir = 1000000000 # Default=750
    DarkElixir = 1000000000 # Default=0
    Diamonds = 1000000000 # Default=500
    FreeDiamonds = 0 # Default=0
    AttackRating = 0 # Default=0
    AttackKFactor = 0 # Default=0
    Score = 3200 # Default=0
    LeagueType = LeagueUtils.GetLeagueByScore(Score) # Default=0
    AttackWinCount = 0 # Default=0
    AttackLoseCount = 0 # Default=0
    DefenseWinCount = 0 # Default=0
    DefenseLoseCount = 0 # Default=0
    NameSetByUser = 0 # Default=0
    CumulativePurchasedDiamonds = 0 # Default=0
    TutorialSteps = 0



    State = 'Home' # Home, Battle

    def __init__(self, device):
        self.device = device

    def encode(self):
        return None