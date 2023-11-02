$(document).ready(function() {
  $('#add_item').click(function() {
    const $list = $('ul.my_list');
    const $newListItem = $('<li>Item</li>');
    $list.append($newListItem);
  });

  $('#remove_item').click(function() {
    $('ul.my_list li:last-child').remove();
  });

  $('#clear_list').click(function() {
    $('ul.my_list').empty();
  });
});
