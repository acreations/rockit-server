define(['angular-translate', 'angular-translate-loader'], function () {
  'use strict';

  return ['$translateProvider', function ($translateProvider) {
    $translateProvider.useLoader('$translatePartialLoader', {
      urlTemplate: '/static/resources/i18n/{lang}/{part}.json'
    });
    $translateProvider.preferredLanguage('en');
  }];
});