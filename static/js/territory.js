(function() {
  $('#territory-dropdown li:first').each(function() {
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
  $('#new-terr-save').click(function() {
    alert('We need the API for creating a new territory');
    $("#newTerrModal").modal('hide');
  });
})();