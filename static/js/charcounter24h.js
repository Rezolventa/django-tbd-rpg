/*

 Helps user to keep long strings short
 by displaying a remain characters count during the typing.

 Usage:
 1. Add "<span id="<LABEL_ID>" class="pull-right"></span>" on a form
 2. Add th folowing in a "more_scripts" block of the template:

    <script src="{% static "tvadmin/js/charcounter24h.js" %}"></script>
    let descrLimit = <SOFT_LIMIT>;
    let descrInput = $(<INPUT_ID>);
    let counterLabel = $(<LABEL_ID>);
    updateCharHelper(descrInput, counterLabel, descrLimit);
    descrInput.keyup(function () {
        updateCharHelper(descrInput, counterLabel, descrLimit);
    });

 */

function updateCharHelper(descrInput, counterLabel, limit) {
    let remain_chars = limit - descrInput.val().length;

    if (remain_chars > 20) {
        counterLabel.addClass('text-muted');
        counterLabel.removeClass('text-danger');
        counterLabel.removeClass('text-warning');

    } else if (remain_chars > 0) {
        counterLabel.addClass('text-warning');
        counterLabel.removeClass('text-danger');
        counterLabel.removeClass('text-muted');

    } else {
        counterLabel.addClass('text-danger');
        counterLabel.removeClass('text-muted');
        counterLabel.removeClass('text-warning');
    }
    counterLabel.text(remain_chars);
}
