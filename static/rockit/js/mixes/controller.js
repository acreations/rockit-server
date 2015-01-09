define(['jquery'], function ($) {
  'use strict';

  return ['$scope', '$log', '$timeout', 'MixesService', 'RockitTranslateService', function (scope, log, timeout, service, translate) {

    translate.addPart("mixes");

    scope.criteria = {};

    scope.getCriterias = function () {

      var createContainer = function (id, groups) {
        return {
          id: id,
          groups: groups,
          selection: {},
          loading: {}
        };
      };

      scope.loading = true;
      service.list().then(
        function (data) {
          log.debug('Successful retrieved mixes criteria', data);

          scope.when = createContainer('when', data.when);
          scope.then = createContainer('then', data.then);
          scope.finish = createContainer('finsih', data.finish);
        },
        function () {
          log.error('Exception when trying to get associations');
        }
      ).finally(function () {
        scope.loading = false;
      });
    };

    scope.onSelectCriteria = function (container, item, anchorID) {
      container.selection.criteria = item;

      log.debug('Trying to get detailed info about', container.selection.criteria.identifier);

      container.loading.criteria = true;
      service.get(item.url).then(
        function (data) {
          log.debug('Successfully retrieved detailed info', data);

          container.criteria = data;

          console.log(container);

          scope.scrollTo(anchorID);
        },
        function () {
          log.error('Exception when trying to get detailed info about', container.selection.criteria.identifier);
        }
      ).finally(function () {
        container.loading.criteria = false;
      });
    };

    scope.toggleGroup = function (container, item, anchorID) {
      // Reset criteria for selected container/group
      scope.criteria[container.id] = false;

      // Either select it or toggle it
      container.selection.group = container.selection.group === item ? null : item;

      // Scroll to anchor
      scope.scrollTo(anchorID);
    };

    scope.scrollTo = function (id) {
      timeout(function () {
        $('html, body').animate({
          scrollTop: $(id).offset().top
        }, 1000);
      }, 0);
    };

  }];
});