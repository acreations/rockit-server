define(['jquery'], function ($) {
  'use strict';

  return ['$scope', '$log', '$timeout', 'MixResource', 'RockitTranslateService', function (scope, log, timeout, Mix, translate) {

    translate.addPart("mixes");

    var collectCriterias = function (holder, container) {
      var _holder = holder[container.id];

      if (!_holder) {
        log.error('Cannot find holder, skip saving', container);
        return;
      }

      if (!container.skipped && container.criteria.actions.POST) {
        var values = [];
        angular.forEach(container.criteria.actions.POST, function (criteria) {
          values.push({
            id: criteria.id,
            value: criteria.model
          });
        });

        _holder.push({
          id: container.selection.criteria.identifier,
          values: values
        });
      }
    };

    var collectPersonalization = function (holder, container) {
      holder.name = container.name;
      holder.description = container.description || '';
    };

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
      Mix.get().then(
        function (data) {
          log.debug('Successful retrieved mixes criteria', data);

          scope.when = createContainer('when', data.when);
          scope.then = createContainer('then', data.then);
          scope.finish = createContainer('finish', data.finish);
          scope.personalize = {
            'name': '',
            'description': ''
          };
        },
        function () {
          log.error('Exception when trying to get associations');
        }
      ).finally(function () {
        scope.loading = false;
      });
    };

    scope.next = function (container, anchorID) {
      log.debug('Trying to validate container', container);

      var hasError = false;

      if (container.criteria.actions.POST) {
        angular.forEach(container.criteria.actions.POST, function (criteria) {
          scope.validateCriteria(criteria);

          if (!hasError && criteria.error) {
            hasError = hasError || criteria.error;
          }
        });
      }

      container.criteria.hasError = hasError;

      container.saved = true;

      log.debug('Container has errors', hasError);

      if (!hasError) {
        scope.scrollTo(anchorID);
      }
    };

    scope.onSelectCriteria = function (container, item, anchorID) {
      container.selection.criteria = item;

      log.debug('Trying to get detailed info about', container.selection.criteria.identifier);

      container.loading.criteria = true;
      Mix.criteria(item.url).then(
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
      // Reset skipped
      container.skipped = false;

      // Set as saved
      container.saved = false;

      // Either select it or toggle it
      container.selection.group = container.selection.group === item ? null : item;

      // Scroll to anchor
      scope.scrollTo(anchorID);
    };

    scope.save = function () {

      var post = {
        'when': [],
        'then': [],
        'finish': []
      };

      collectPersonalization(post, scope.personalize);
      collectCriterias(post, scope.when);
      collectCriterias(post, scope.then);
      collectCriterias(post, scope.finish);

      log.debug('Trying to save action', post);
      Mix.save(post).then(
        function (data) {
          log.debug('Successfully saved mix', data);
        },
        function () {
          log.error('Failed to save mix');
        }
      );
    };

    scope.skip = function (container, anchorID) {
      // Set skipped state
      container.skipped = true;

      // Set as saved
      container.saved = true;

      // Reset selection
      container.selection = {};

      // Reset criteria set
      container.criteria = null;

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

    scope.validateCriteria = function (criteria) {
      if (criteria.required) {
        criteria.error = !criteria.model || criteria.model === '';
      }
    };

  }];
});