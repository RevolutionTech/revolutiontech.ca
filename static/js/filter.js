$(document).ready(function() {
    'use strict'

    var all_regular_items = $('.item-short-regular').clone();

    $('dd').click(function(){
        // If this one is already active, then ignore
        if ($(this).hasClass('active')) return;

        // Otherwise, deactivate the active class
        $('dd.active').removeClass('active');
        // and set this filter as active
        $(this).addClass('active');

        // Determine the selected category
        var this_classes = $(this).attr('class').split(' ');
        var selected_category = $(this_classes).filter(function(){
            if (this.indexOf('category') == 0) return true;
            return false;
        })[0];

        // Filter items in the category
        var filtered_items = all_regular_items.filter(function(){
            if (selected_category == 'category-all'
                || $(this).hasClass(selected_category)) return true;
            return false;
        });

        // Remove all items
        $('.item-short-regular').remove();

        // Re-enter filtered items
        $('.items-short-regular').append(filtered_items);
    });
});
