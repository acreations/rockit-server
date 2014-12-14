define(['toastr'], function (toastr) {
  'use strict';

  /* Configure toastr */
  toastr.options = {
    "closeButton": false,
    "debug": false,
    "progressBar": true,
    "positionClass": "toast-bottom-full-width",
    "onclick": null,
    "showDuration": "300",
    "hideDuration": "500",
    "timeOut": "3000",
    "extendedTimeOut": "1000",
    "showEasing": "swing",
    "hideEasing": "swing",
    "showMethod": "fadeIn",
    "hideMethod": "fadeOut"
  };

  return [function () {
    return toastr;
  }];
});