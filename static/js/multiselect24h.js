let multiSelectOptions = {
    selectableHeader: '<input type="text" class="form-control search-input" autocomplete="off" placeholder="Search">',
    selectionHeader: '<input type="text" class="form-control search-input" autocomplete="off" placeholder="Search">',

    afterInit: function (ms) {
        var that = this,
            $selectableSearch = that.$selectableUl.prev(),
            $selectionSearch = that.$selectionUl.prev(),
            selectableSearchString = '#' + that.$container.attr('id') + ' .ms-elem-selectable:not(.ms-selected)',
            selectionSearchString = '#' + that.$container.attr('id') + ' .ms-elem-selection.ms-selected';

        that.qs1 = $selectableSearch.quicksearch(selectableSearchString)
            .on('keydown', function (e) {
                if (e.which === 40) {
                    that.$selectableUl.focus();
                    return false;
                }
            });

        that.qs2 = $selectionSearch.quicksearch(selectionSearchString)
            .on('keydown', function (e) {
                if (e.which == 40) {
                    that.$selectionUl.focus();
                    return false;
                }
            });
    },
    afterSelect: function () {
        this.qs1.cache();
        this.qs2.cache();
    },
    afterDeselect: function () {
        this.qs1.cache();
        this.qs2.cache();
    }
};

function multiSelect24h(element_id) {
    let selectionFooter = `
    <div class="form-group text-right m-t-10 m-b-0">
        <button type="button" id="my_button" onclick="multiSelect24h_Scope('` + element_id + `', 'deselect_all');" class="btn btn-xs btn-rounded btn-primary">
            <i class="fa fa-arrow-left"></i>
        </button>
        <button type="button" onclick="multiSelect24h_Scope('` + element_id + `', 'select_all');" class="btn btn-xs btn-rounded btn-primary">
            <i class="fa fa-arrow-right"></i>
        </button>
    </div>`;

    multiSelectOptions['selectionFooter'] = selectionFooter;

    $(element_id).multiSelect(multiSelectOptions);
}

function multiSelect24h_Scope(element_id, action) {
    $(element_id).multiSelect(action);
}
