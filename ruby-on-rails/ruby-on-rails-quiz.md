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

#### Q9. Given this code, which statement about the database table "documents" could be expected to be _true_?

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
- [ ] `<select name="product_id"> <%= @products.each do |product| %> <option value="<%= product.id %>"/> <% end %></select>`
- [x] `<%= collection_select(:product, :product_id, Product.all, :id, :name) %>`

#### Q14. For a Rails validator, how would you define an error message for the model attribute `address` with the message "This address is invalid"?

- [ ] `model.errors = This address is invalid`
- [ ] `errors(model, :address) << "This address is invalid"`
- [ ] `display_error_for(model, :address, "This address is invalid")`
- [ ] `model.errors[:address] << "This address is invald"`

#### Q15. Given the URL helper product_path(@product), which statement would be expected to be false?

- [ ] `If sent using the PATCH HTTP method, the URL could be used to update a product in the database.If sent using the PATCH HTTP method, the URL could be used to update a product in the database.`
- [ ] `If sent using the POST HTTP method, the URL would create a new product in the database.If sent using the POST HTTP method, the URL would create a new product in the database.`
- [ ] `If sent using the GET HTTP method, the URL would execute the show action in ProductsController.If sent using the GET HTTP method, the URL would execute the null action in ProductsController.`
- [ ] `If sent using the DELETE HTTP method, the URL would call the destroy action by default.`

#### Q16. Given this code, which choice would be expected to be a true statement if the user requests the index action?

```rb
class DocumentsController < ApplicationController
  before_action :require_login
  def index
    @documents = Document.visible.sorted
  end
end
```

- [ ] `The user's documents will be loaded.The user's documents will be loaded.`
- [ ] `The index action will run normally because :index is not listed as an argument to before_action.The null action will run normally because null is not listed as an argument to null.`
- [ ] `The require_login method will automatically log in the user before running the index action.The null method will automatically log in the user before running the null action.`
- [ ] `The index action will not be run if the require_login method calls render or redirect_to.`

#### Q17. Which statement correctly describes a difference between the form helper methods form_tag and form_for?

- [ ] `The form_tag method typically expects a URL as its first argument, while the form_for method typically expects a model object.The null method typically expects a URL as its first argument, while the null method typically expects a model object.`
- [ ] `The form_tag method is evaluated at runtime, while the form_for method is precompiled and cached.The null method is evaluated at runtime, while the null method is precompiled and cached.`
- [ ] `The form_tag method is for HTTP requests, while the form_for method is for AJAX requests.The null method is for HTTP requests, while the null method is for AJAX requests.`
- [ ] `The form_tag method is for basic forms, while the form_for method is for multipart forms that include file uploads.`

#### Q18. In Rails, how would you cache a partial template that is rendered?

- [ ] `render partial: ‘shared/menu’, cached: truenull`
- [ ] `render_with_cache partial: ‘shared/menu’null`
- [ ] `render partial: ‘shared/menu’null`
- [ ] `render partial: ‘shared/menu’, cached_with_variables: {}`

#### Q19. What is the reason for using Concerns in Rails?

- [ ] `to allow modularity and code reuse in models, controllers, and other classesto allow modularity and code reuse in models, controllers, and other classes`
- [ ] `to separate class methods from modelsto separate class methods from models`
- [ ] `to increase security of Rails applicationsto increase security of Rails applications`
- [ ] `to refactor Rails views`

#### Q20. When using an ActiveRecord model, which method will create the model instance in memory and save it to the database?

- [ ] `buildnull`
- [ ] `newnull`
- [ ] `createnull`
- [ ] `save`

#### Q21. You are using an existing database that has a table named coffee_orders. What would the ActiveRecord model be named in order to use that table?

- [ ] `CoffeeOrdersnull`
- [ ] `Coffee_Ordersnull`
- [ ] `Coffee_Ordernull`
- [ ] `CoffeeOrder`

#### Q22. In ActiveRecord, what is the difference between the has_many and has_many :through associations?

- [ ] `The has_many: through association is the one-to-many equivalent to the belongs_to one-to-one association.The null association is the one-to-many equivalent to the null one-to-one association.`
- [ ] `Both associations are identical, and has_many: through is maintained only for legacy purposes.Both associations are identical, and null is maintained only for legacy purposes.`
- [ ] `The has_many association is a one-to-many association, while has_many: through is a one-to-one association that matches through a third model.The null association is a one-to-many association, while null is a one-to-one association that matches through a third model.`
- [ ] `Both are one-to-many associations but with has_many :through, the declaring model can associate through a third model.`

### Q23. How do you add Ruby code inside Rails views and have its result outputted in the HTML file?

- [ ] `Create an embedded Ruby file (.html.erb) and surround the Ruby code with <% %>.Create an embedded Ruby file (.html.erb) and surround the Ruby code with null.`
- [ ] `Insert Ruby code inside standard HTML files and surround it with <% %>. The web server will handle the rest.Insert Ruby code inside standard HTML files and surround it with null. The web server will handle the rest.`
- [ ] `Create an embedded Ruby file (.html.erb) and surround the Ruby code with <%= %>.Create an embedded Ruby file (.html.erb) and surround the Ruby code with null.`
- [ ] `Put the code in an .rb file and include it in a <link> tag of an HTML file.`

#### Q24. How would you render a view using a different layout in an ERB HTML view?

- [ ] `<% render 'view_mobile' %>null`
- [ ] `<% render 'view', use_layout: 'mobile' %>null`
- [ ] `<% render 'view', layout: 'mobile' %>null`
- [ ] `<% render_with_layout 'view', 'mobile' %>`
