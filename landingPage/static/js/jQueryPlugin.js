window.addEventListener('DOMContentLoaded', (event) => {     console.log('DOM fully loaded and parsed'); 
    $(".search_input").on("keyup",function(event){
        
        var searchTerm = event.target.value.toLowerCase().trim();
        var eventDescriptions = $(".description");
        $.each(eventDescriptions,(index,description) => {
            //console.log(description);
            var eventDescription = description.innerHTML.toLowerCase().trim();
            if(eventDescription.includes(searchTerm)){
                //console.log("Matsy matsy");
                $(description).closest(".eventrow").fadeIn(144);

            }else{
                $(description).closest(".eventrow").hide();
            }  
        });
    })
    $(".search_category").on("change",function(event){
        
        var searchTerm = event.target.value;
        var eventCategories = $(".category");
        $.each(eventCategories,(index,category) => {
            //console.log(description);
            var eventCategory = category.innerHTML;
            if(searchTerm === eventCategory || searchTerm == ''){
                //console.log("Matsy matsy");
                $(category).closest(".eventrow").fadeIn(144);
            }else{
                $(category).closest(".eventrow").hide();
            }
        });
    })
    $(".greetings").on("click",()=>{
        $(".user_details_form").show()
        console.log("clicked")
    })
});