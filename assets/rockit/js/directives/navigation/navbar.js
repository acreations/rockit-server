define(['jquery'], function ($) {
  'use strict';

  return ['$rootScope', '$location', '$window', '$document', function ($rootScope, $location, window, document) {
    return {
      restrict: 'C',
      translude: true,
      controller: function ($scope) {
        $rootScope.$on('$locationChangeSuccess', function () {
          $scope.path = $location.path().split('/')[1];
        });
      },
      link: function (scope, element) {
        var w = $(window);
        var e = $(element);

        var lastScrollTop = 0;
        var KI_OFFSET = 10;

        w.bind('scroll', function () {
          var st = w.scrollTop();

          if (Math.abs(lastScrollTop - st) > KI_OFFSET) {
            if (st > lastScrollTop) {
              if (st > 0) {
                e.fadeOut();
              }
            } else {
              e.fadeIn();
            }

            lastScrollTop = st;
          }
        });
      }
    };
  }];
});