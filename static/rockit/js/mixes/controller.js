define(['jquery'], function ($) {
  'use strict';

  return ['$scope', '$log', 'MixesService', function (scope, log, service) {

    scope.criteria = {};

    var onCreate = function () {
      scope.getCriterias();
    };

    scope.onSelectWhen = function (item) {
      var identifier = item.identifier;

      log.debug('Trying to get detailed info about', identifier);
      service.get(item.url).then(
        function (data) {
          log.debug('Successfully retrieved detailed info', data);

          scope.criteria.when = data;

          console.log(scope.criteria);
        },
        function () {
          log.error('Exception when trying to get detailed info about', identifier);
        }
      );
    };

    scope.toggle = function (container, item, anchorID) {
      // Reset criteria for selected container/group
      scope.criteria[container.id] = false;

      // Either select it or toggle it
      container.selected = container.selected === item ? null : item;
    };

    scope.getCriterias = function () {
      service.list().then(
        function (data) {
          log.debug('Successful retrieved mixes criteria', data);

          scope.when = {
            id: 'when',
            data: data.when
          };
        },
        function () {
          log.error('Exception when trying to get associations');
        }
      );
    };

    scope.scrollTo = function (id) {
      $('html, body').animate({
        scrollTop: $(id).offset().top
      }, 1000);
    }

    onCreate();
  }];
});