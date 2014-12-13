define([], function () {
  'use strict';

  return ['$translatePartialLoader', '$translate', function (loader, translate) {
    return {
      addPart: function (resource) {
        loader.addPart(resource);
        translate.refresh();
      }
    };
  }];
});