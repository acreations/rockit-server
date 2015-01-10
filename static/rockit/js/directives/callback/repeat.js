define([], function () {
  'use strict';

  return ['$timeout', function (timeout) {
    return {
      restrict: 'A',
      link: function (scope, element, attrs) {
        if (scope.$last === true) {
          timeout(function () {
            scope.$emit('onRepeatDone', element, attrs);
          }, 0);
        }
      }
    };
  }];
});