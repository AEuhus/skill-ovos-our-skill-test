from ovos_utils import classproperty
from ovos_utils.log import LOG
from ovos_workshop.intents import IntentBuilder
from ovos_utils.process_utils import RuntimeRequirements
from ovos_workshop.decorators import intent_handler
from ovos_workshop.skills import OVOSSkill


DEFAULT_SETTINGS = {
    "log_level": "WARNING"
}


class ScienceFairProject(OVOSSkill):
    def __init__(self, *args, **kwargs):
        """The __init__ method is called when the Skill is first constructed.
        Note that self.bus, self.skill_id, self.settings, and
        other base class settings are only available after the call to super().
        """
        super().__init__(*args, **kwargs)
        # be aware that below is executed after `initialize`
        self.override = True

    @classproperty
    def runtime_requirements(self):
        return RuntimeRequirements(
            internet_before_load=True,
            network_before_load=True,
            gui_before_load=False,
            requires_internet=True,
            requires_network=True,
            requires_gui=False,
            no_internet_fallback=False,
            no_network_fallback=False,
            no_gui_fallback=True,
        )
    
    def initialize(self):
        """Performs any final setup of the Skill, for instance to register
        handlers for events that the Skill will respond to.
        This is a good place to load and pre-process any data needed by your Skill.
        """
        # This initializes a settings dictionary that the skill can use to
        # store and retrieve settings. The skill_settings.json file will be
        # created in the location referenced by self.settings_path, which
        # defaults to ~/.config/mycroft/skills/<skill_id>
        # only new keys will be added, existing keys will not be overwritten
        self.settings.merge(DEFAULT_SETTINGS, new_only=True)
        # set a callback to be called when settings are changed
        self.settings_change_callback = self.on_settings_changed
        # (custom) event handler setup example
        # below is a custom event, system event specs found at
        # https://openvoiceos.github.io/message_spec/
        # this can be tested using `mana` (https://github.com/NeonGeckoCom/neon-mana-utils)
        # `mana send-message hello.world`
        self.add_event("fav.subnautica.creature", self.handle_fav_subnaut_creature_intent)
        self.my_var = "alex is fat"

    def on_settings_changed(self):
        """This method is called when the skill settings are changed."""
        LOG.info("Settings changed!")

    @property
    def log_level(self):
        """Dynamically get the 'log_level' value from the skill settings file.
        If it doesn't exist, return the default value.
        This will reflect live changes to settings.json files (local or from backend)
        """
        return self.settings.get("log_level", "INFO")

    @intent_handler("AlexIsFat.intent")
    def handle_alex_is_fat_intent(self, message):
        self.speak_dialog("alex.is.fat")
        LOG.info(("There are five types of log messages: 'info, debug, warning, ")
                 ("error, and exception."))
        if self.log_level == "WARNING":
            LOG.warning(("To be able to see debug logs, you need to change the")
                        ("'log_level' setting to 'DEBUG' in the core ")
                        ("configuration (mycroft.conf)"))

    @intent_handler("ChatGPTThoughts.intent")
    def handle_chat_gpt_thoughts_intent(self, message):
        self.speak_dialog("chat.gpt.thoughts")
        LOG.info(("There are five types of log messages: 'info, debug, warning, ")
                 ("error, and exception."))
        if self.log_level == "WARNING":
            LOG.warning(("To be able to see debug logs, you need to change the")
                        ("'log_level' setting to 'DEBUG' in the core ")
                        ("configuration (mycroft.conf)"))

    @intent_handler("FavFood.intent")
    def handle_fav_food_intent(self, message):
        self.speak_dialog("fav.food")
        LOG.info(("There are five types of log messages: 'info, debug, warning, ")
                 ("error, and exception."))
        if self.log_level == "WARNING":
            LOG.warning(("To be able to see debug logs, you need to change the")
                        ("'log_level' setting to 'DEBUG' in the core ")
                        ("configuration (mycroft.conf)"))
 
    @intent_handler("FavMusic.intent")
    def handle_fav_music_intent(self, message):
        self.speak_dialog("fav.music")
        LOG.info(("There are five types of log messages: 'info, debug, warning, ")
                 ("error, and exception."))
        if self.log_level == "WARNING":
            LOG.warning(("To be able to see debug logs, you need to change the")
                        ("'log_level' setting to 'DEBUG' in the core ")
                        ("configuration (mycroft.conf)"))

    @intent_handler("FavSubnautCreature.intent")
    def handle_fav_subnaut_creature_intent(self, message):
        self.speak_dialog("fav.subnaut.creature")
        LOG.info(("There are five types of log messages: 'info, debug, warning, ")
                 ("error, and exception."))
        if self.log_level == "WARNING":
            LOG.warning(("To be able to see debug logs, you need to change the")
                        ("'log_level' setting to 'DEBUG' in the core ")
                        ("configuration (mycroft.conf)"))

    @intent_handler("HelloWorld.intent")
    def handle_hello_world_intent(self, message):
        self.speak_dialog("hello.world")
        LOG.info(("There are five types of log messages: 'info, debug, warning, ")
                 ("error, and exception."))
        if self.log_level == "WARNING":
            LOG.warning(("To be able to see debug logs, you need to change the")
                        ("'log_level' setting to 'DEBUG' in the core ")
                        ("configuration (mycroft.conf)"))

    @intent_handler("HowIsDay.intent")
    def handle_how_is_day_intent(self, message):
        self.speak_dialog("how.is.day")
        LOG.info(("There are five types of log messages: 'info, debug, warning, ")
                 ("error, and exception."))
        if self.log_level == "WARNING":
            LOG.warning(("To be able to see debug logs, you need to change the")
                        ("'log_level' setting to 'DEBUG' in the core ")
                        ("configuration (mycroft.conf)"))


    @intent_handler("InventHoliday.intent")
    def handle_invent_holiday_intent(self, message):
        self.speak_dialog("invent.holiday")
        LOG.info(("There are five types of log messages: 'info, debug, warning, ")
                 ("error, and exception."))
        if self.log_level == "WARNING":
            LOG.warning(("To be able to see debug logs, you need to change the")
                        ("'log_level' setting to 'DEBUG' in the core ")
                        ("configuration (mycroft.conf)"))

    @intent_handler("NFLTeams.intent")
    def handle_nfl_teams_intent(self, message):
        self.speak_dialog("nfl.teams")
        LOG.info(("There are five types of log messages: 'info, debug, warning, ")
                 ("error, and exception."))
        if self.log_level == "WARNING":
            LOG.warning(("To be able to see debug logs, you need to change the")
                        ("'log_level' setting to 'DEBUG' in the core ")
                        ("configuration (mycroft.conf)"))

    @intent_handler("PrincessPea.intent")
    def handle_princess_pea_intent(self, message):
        self.speak_dialog("princess.pea")
        LOG.info(("There are five types of log messages: 'info, debug, warning, ")
                 ("error, and exception."))
        if self.log_level == "WARNING":
            LOG.warning(("To be able to see debug logs, you need to change the")
                        ("'log_level' setting to 'DEBUG' in the core ")
                        ("configuration (mycroft.conf)"))

    @intent_handler("ThanksForTalking.intent")
    def handle_thanks_for_talking_intent(self, message):
        self.speak_dialog("thanks.for.talking")
        LOG.info(("There are five types of log messages: 'info, debug, warning, ")
                 ("error, and exception."))
        if self.log_level == "WARNING":
            LOG.warning(("To be able to see debug logs, you need to change the")
                        ("'log_level' setting to 'DEBUG' in the core ")
                        ("configuration (mycroft.conf)"))
                    

    @intent_handler("TortoiseHare.intent")
    def handle_tortoise_hare_intent(self, message):
        self.speak_dialog("tortoise.hare")
        LOG.info(("There are five types of log messages: 'info, debug, warning, ")
                 ("error, and exception."))
        if self.log_level == "WARNING":
            LOG.warning(("To be able to see debug logs, you need to change the")
                        ("'log_level' setting to 'DEBUG' in the core ")
                        ("configuration (mycroft.conf)"))

    @intent_handler("WhatMadeLaugh.intent")
    def handle_what_made_laugh_intent(self, message):
        self.speak_dialog("what.made.laugh")
        LOG.info(("There are five types of log messages: 'info, debug, warning, ")
                 ("error, and exception."))
        if self.log_level == "WARNING":
            LOG.warning(("To be able to see debug logs, you need to change the")
                        ("'log_level' setting to 'DEBUG' in the core ")
                        ("configuration (mycroft.conf)"))

    @intent_handler("WhatMadeSad.intent")
    def handle_what_made_sad_intent(self, message):
        self.speak_dialog("what.made.sad")
        LOG.info(("There are five types of log messages: 'info, debug, warning, ")
                 ("error, and exception."))
        if self.log_level == "WARNING":
            LOG.warning(("To be able to see debug logs, you need to change the")
                        ("'log_level' setting to 'DEBUG' in the core ")
                        ("configuration (mycroft.conf)"))

    def stop(self):
        """Optional action to take when "stop" is requested by the user.
        This method should return True if it stopped something or
        False (or None) otherwise.
        If not relevant to your skill, feel free to remove.
        """
        pass
