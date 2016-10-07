  ///config.forcePasteAsPlainText = true; /// true

  config.pasteFromWordIgnoreFontFace = true;
  config.pasteFromWordRemoveStyle = true;
  config.pasteFromWordKeepsStructure = false; /* CleanWordKeepsStructure = false; // FCKEditor?? */

  // @see http://docs.cksource.com/ckeditor_api/symbols/CKEDITOR.config.html#.entities
  config.entities_latin = true; // DEFAULT: for NAMED-html-entities

  config.entities_additional = /* '#39'; */ '#8217,#8218,#8220,#8221';
  //config.entities_greek = true;             /// WIP
  config.entities_processNumerical = true;  /// WIP


  config.toolbar_PnNONE = [[ ]];

  config.toolbar_PnBASIC_Word = [[ 'Bold', 'Italic', 'Underline', 'Strike',
    '-', 'NumberedList', 'BulletedList',
    '-', 'Link', 'Unlink',
    '-', 'Cut', 'Copy', 'Paste',
    //'-', 'PasteText', 'PasteFromWord',
    '-', 'SelectAll', 'RemoveFormat',
    '-', 'SpellChecker', 'Scayt',
    '-', 'ShowBlocks', 'Preview',
  //'-', 'Source',
    '-', 'Maximize'
  ]];
  //config.toolbar = 'PnBASIC_Word'; // ie. GLOBAL setting

  config.toolbarStartupExpanded = false;
  //config.toolbarCanCollapse = false;
