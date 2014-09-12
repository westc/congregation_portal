(function () {
    $('#territory-dropdown li:first').each(function () {
        // Put "Add Territory" in the "Territory Manager" dropdown menu.
        $(this)
            .clone(true, true)
            .find('a')
            .attr('href', 'javascript://')
            .text('Add Territory')
            .click(showNewTerrModal)
            .end()
            .insertBefore(this);
    });

    // Shows a modal to create a new territory.
    function showNewTerrModal() {
        $("#newTerrModal").modal();
    }

    // Set up "Create Territory" button.
    $('#new-terr-save').click(function () {
        var new_terr_num = $('#new-terr-num').val();
        var new_terr_name = $('#new-terr-name').val();
        var new_terr_type = $('#new-terr-type').val();

        // TODO: Display friendlier errors using bootstrap theme error notifications.
        if (!new_terr_num || !parseInt(new_terr_num)) {
            alert("Number missing or not an int.");
            return;
        }

        if (!new_terr_name) {
            alert("Name missing.");
            return;
        }

        if (!new_terr_type) {
            alert("Type missing.");
            return;
        }

        $.ajax({
            type: "POST",
            url: "/api/territory/",
            data: {
                number: new_terr_num,
                name: new_terr_name,
                type: new_terr_type
            }
        }).success(function () {
            loadTerrList();
            $("#newTerrModal").modal('hide');
        }).error(function (response) {
            alert(response);
        });
    });

    $('#btnAddHouse').click(showNewTerrItemModal);

    function showNewTerrItemModal() {
        $("#newTerrItemModal").modal();
    }

    function addTerrToList(terr) {
        var type = 
        $('#' + (terr['type'] == 'H' ? 'home' : 'phone') + 'TerrList').append(
            $('<li>').append(
                $('<div class="news-item-detail">').append(
                    $('<a href="javascript:;" class="news-item-title">')
                        .text('#' + terr.number + ' - ' + terr.name)
                )
            ).append(
                $('<div class="news-item-date">').append(
                    $('<span class="news-item-day">')
                        .text(terr.items.length)
                ).append(
                    $('<span class="news-item-month">')
                        .text((terr['type'] == 'H' ? 'house' : 'number') + (terr.items.length - 1 ? 's' : ''))
                )
            )
        );
    }

    // Load territory list
    function loadTerrList() {
        $.getJSON('/api/territory/', function(arr, status, xhr) {
            $('#homeTerrList, #phoneTerrList').html("");
            arr.forEach(addTerrToList);
        });
    }

    loadTerrList();

    // POST /api/territory/1/item/ => create new item for specific territory
    // Sample request
    //     {
    //         "phone_number": "", 
    //         "address1": "25 Monmouth St.", 
    //         "address2": "", 
    //         "city": "Red Bank", 
    //         "state": "NJ", 
    //         "notes": ""
    //     } 
})();