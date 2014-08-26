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

        if (!new_terr_num || !parseInt(new_terr_num)) {
            alert("TODO: nicer error message. Number missing or not an int.");
            return;
        }

        if (!new_terr_name) {
            alert("TODO: nicer error message. Name missing.");
            return;
        }

        if (!new_terr_type) {
            alert("TODO: nicer error message. Type missing.");
            return;
        }

        $.ajax({
            type: "POST",
            url: "/api/territory/",
            data: {number: new_terr_num,
                name: new_terr_name,
                type: new_terr_type}
        }).success(function () {
            $("#newTerrModal").modal('hide');
        }).error(function (response) {
            alert(response);
        });
    });

    // Load territory list
    $.ajax({
        type: "GET",
        url: "/api/territory/"
    }).success(function (response) {
        console.log(response);
    });

})();