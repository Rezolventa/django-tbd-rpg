!function ($) {
    "use strict";
    var SweetAlert = function () {
    };
    SweetAlert.prototype.init = function () {

        $('.js-delete-confirm').on('click',function(e){
            var button = $(this);
            swal({
                title: "Вы уверены, что хотите удалить?",
                type: "error",
                text: "Данное действие нельзя будет обратить!",
                showCancelButton: true,
                cancelButtonClass: 'btn-default waves-effect waves-light',
                confirmButtonClass: 'btn-danger waves-effect waves-light',
                confirmButtonText: 'Удалить',
                cancelButtonText: "Отменить",
                closeOnConfirm: false,
                closeOnCancel: true
                }, function () {
                    button.off('click');
                    button.click();
                });
                return false;
            });

            $('.js-execute-confirm').on('click',function(e){
            var button = $(this);
            swal({
                title: "Вы уверены?",
                type: "info",
                text: "Данное действие нельзя будет обратить!",
                showCancelButton: true,
                cancelButtonClass: 'btn-default waves-effect waves-light',
                confirmButtonClass: 'btn-danger waves-effect waves-light',
                confirmButtonText: 'Выполнить',
                cancelButtonText: "Отменить",
                closeOnConfirm: false,
                closeOnCancel: true
                }, function () {
                    button.off('click');
                    button.click();
                });
                return false;
            });
    },
    $.SweetAlert = new SweetAlert, $.SweetAlert.Constructor = SweetAlert
}(window.jQuery),
    function ($) {
        "use strict";
        $.SweetAlert.init()
    }(window.jQuery);
