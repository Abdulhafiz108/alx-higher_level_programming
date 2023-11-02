$(document).ready(function() {
  $('#add_item').click(function() {
    const $list = $('ul.my_list');
    const $newListItem = $('<li>Item</li>');
    $list.append($newListItem);
  });
});
