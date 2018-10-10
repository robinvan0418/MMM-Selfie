/* global Module */

/* Magic Mirror
 * Module: MMM-Selfie
 *
 * By Alberto de Tena Rojas http://albertodetena.com
 * MIT Licensed.
 */

Module.register('MMM-Selfie',
{
	defaults:
	{
    useUSBCam: false,
    maxResX: 2592,
    maxResY: 1944,
    cameraRotation: 90,
    Facebook_pageid: '',
    Facebook_token: '',
    Facebook_ProfileId: '',
    twitter_access_key: '',
    twitter_access_secret: '',
    twitter_consumer_key: '',
    twitter_consumer_secret: ''
  },

	// Define required translations.
	getTranslations: function() {
		return {
			en: "translations/en.json",
      es: "translations/es.json",
			fr: "translations/fr.json"
		};
	},

	getCommands : function(register) {
    if (register.constructor.name == 'TelegramBotCommandRegister') {
      register.add({
        command: 'selfie',
        description: this.translate("CMD_TELBOT_SELFIE"),
        callback: 'cmd_selfie'
      })
    }
    if (register.constructor.name == 'AssistantCommandRegister') {
      register.add({
        command: this.translate("CMD_ASSTNT_SELFIE"),
        description: this.translate("CMD_ASSTNT_SELFIE_DESCRIPTION"),
        callback: 'cmd_selfie'
      })
    }
  },

  cmd_selfie : function (command, handler)
	{
      Log.info('Trying to get a Selfie');
      this.config.args = handler.args;
      this.config.message = handler.message;
      this.config.callbacks = handler.callbacks;
      if (this.config.args != "")
      {
        this.config.new_status = this.config.args;
      }
      else
      {
        this.config.new_status = this.config.message.substr(7);
      }
    	handler.reply('TEXT','Trying to get a selfie...');
    	$.when(function() {this.sendSocketNotification('SELFIE', this.config)}).then(function() {
			handler.reply("PHOTO_PATH", "/home/pi/MagicMirror/modules/MMM-Selfie/selfie.jpg", {caption:"Coolest Selfie!"})
		});
		
		
 	},

	start: function()
	{
	  Log.info('Starting module: ' + this.name);
	}
});
