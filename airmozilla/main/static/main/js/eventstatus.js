$(function () {
    var currentEventStatus = $('.entry-content').data('event-status');

    var interval = setInterval(function () {
        $.get(location.pathname + 'status/')
            .then(function (data) {
                if (currentEventStatus !== data.status) {
                    location.reload();
                }
            })
            .fail(function () {
                console.error("Failed to fetch event status. Stops looking.");
                clearInterval(interval);
            });
    }, 10 * 1000);
});
