## Ruby on Rails Assessment

#### Q1. When rendering a partial in a view, how would you pass local variables for rendering?

- [ ] `<%= render partial: "nav", selected: "about"}%>`
- [ ] `<%= render partial: "nav", local_variabels: {selected: "about"} %>`
- [ ] `<%= render partial: "nav", locals: {selected: "about"}`
- [ ] `<%= render partial: "nav", locals: {selected: "about"}`

#### Q2. Within a Rails controller, which code will prevent the parent controller's before_action `:get_feature:` from running?

- [ ] `skip_before_action :get_feature`
- [x] `skip :get_feature, except: []`
- [ ] `prevent_action :get_feature`
- [ ] `redis_cache_store`

#### Q3. Which statement correctly describes a difference between the form helper methods `form_tag` and `form_for`?

- [ ] The `form_tag` method is for basic forms, while the `form_for` method is for multipart forms that include file uploads.
- [ ] The `form_tag` method is for HTTP requests, while the `form_for` method is for AJAX requests.
- [x] The `form_tag` method typically expects a URL as its first argument, while the `form_for` method typically expects a model object.
- [ ] The `form_tag` method is evaluated at runtime, while the `form_for` method is precompiled and cached.

#### Q4. What is `before_action` (formerly known as `before_filter`)?

- [ ] A trigger that is executed before an alteration of an object's state
- [ ] A method that is executed before an ActiveRecord model is saved
- [ ] A callback that fires before an event is handled
- [x] A method in a controller that is executed before the controller action method

#### Q5. Which module can you use to encapsulate a cohesive chunk of functionality into a mixin?

- [ ] `ActiveSupport::Concern`
- [ ] `RailsHelper.CommonClass`
- [ ] `ActiveJob::Mixin`
- [ ] `ActiveSupport::Module`

#### Q6. In Rails, which code would you use to define a route that handles both the `PUT` and `PATCH` `REST HTTP` verbs?

- [ ] put :items, include: patch
- [ ] put 'items', to: 'items#update'
- [ ] match 'items', to 'items#update', via: [:put, :patch]
- [ ] match :items, using: put && patch

#### Q7. Which choice includes standard REST HTTP verbs?

- [x] GET, POST, PATCH, DELETE
- [ ] REDIRECT, RENDER, SESSION, COOKIE
- [ ] INDEX, SHOW, NEW, CREATE, EDIT, UPDATE, DESTROY
- [ ] CREATE, READ, UPDATE, DELETE

#### Q8. Which ActiveRecord query prevents SQL injection?

- [ ] `Product.where("name = #{@keyword}")`
- [ ] `Product.where("name = " << @keyword}`
- [x] `Product.where("name = ?", @keyword`
- [ ] `Product.where("name = " + h(@keyword)`

#### Q9. Given this code, which statement about the database table "documents" could be expected to be *true*?
```rb
class Document < ActiveRecord::Base
    belongs_to :documentable, polymorphic: true
end

class Product < ActiveRecord::Base
    has_many :documents, as: :documentable
end

class Service < ActiveRecord::Base
    has_many :documents, as: :documentable
end
```

- [ ] It would include a column for `:type`.
- [ ] It would include columns for `:documentable_id` and `:documentable_type`.
- [ ] It would include columns for `:documentable` and `:type`.
- [ ] It would include a column for `:polymorphic_type`.

#### Q10. Are instance variables set within a controller method accessible within a view?

- [ ] Yes, any instance variables that are set in an action method on a controller can be accessed and displayed in a view.
- [ ] Yes, instance variables set within an action method are accessible within a view, but only when render is explicitly called inside the action method. 
- [ ] No, instance variables in a controller are private and are not accessible.
- [ ] No, instance variables can never be set in a controller action method. 

#### Q11. When a validation of a field in a Rails model fails, where are the messages for validation errors stored?

- [ ] `my_model.errors[:field]`
- [ ] `my_model.get_errors_for(:field)`
- [ ] `my_model.field.error`
- [ ] `my_model.all_errors.select(:field)`

#### Q12. If a database table of users contains the following rows, and `id` is the primary key, which statement would return only an object whose `last_name` is "Cordero"?
```
------------------------------
id first_name last_name
1 Alice Anderson
2 Bob Buckner
3 Carrie Cordero
4 Devon Dupre
5 Carrie Eastman
------------------------------
```

- [ ] `User.where(first_name: "Carrie")`
- [ ] `User.not.where(id: [1, 2, 4, 5])`
- [ ] `User.find_by(first_name: "Cordero")`
- [x] `User.find(3)`

#### Q13. How would you generate a drop-down menu that allows the user to select from a collection of product names?

- [ ] `<%= select_tag(@products) %>`
- [ ] `<%= collection_select(@products) %>`
- [ ] 
```
<select name="product_id">
    <%= @products.each do |product| %>
        <option value="<%= product.id %>"/>
    <% end %>
</select>
```

- [x] `<%= collection_select(:product, :product_id, Product.all, :id, :name) %>`

#### Q14. For a Rails validator, how would you define an error message for the model attribute `address` with the message "This address is invalid"?

- [ ] `model.errors = This address is invalid`
- [ ] `errors(model, :address) << "This address is invalid"`
- [ ] `display_error_for(model, :address, "This address is invalid")`
- [ ] `model.errors[:address] << "This address is invald"`
