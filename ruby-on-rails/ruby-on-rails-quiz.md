## Ruby on Rails

#### Q1. When rendering a partial in a view, how would you pass local variables for rendering?
- [ ] `<%= render partial: "nav", selected: "about"}%>`
- [ ] `<%= render partial: "nav", local_variables: {selected: "about"} %>`
- [ ] `<%= render partial: "nav", locals: {selected: "about"}`

#### Q2. Within a Rails controller, which code will prevent the parent controller's before_action `:get_feature` from running?
- [ ] `skip_before_action :get_feature`
- [x] `skip :get_feature, except: []`
- [ ] `prevent_action :get_feature`
- [ ] `:redis_cache_store`

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
- [ ] `put :items, include: patch`
- [ ] `put 'items', to: 'items#update'`
- [ ] `match 'items', to 'items#update', via: [:put, :patch]`
- [ ] `match :items, using: put && patch`

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
-------------------------------

| id | first_name | last_name |
|----|------------|-----------|
| 1  | Alice      | Anderson  |
| 2  | Bob        | Buckner   |
| 3  | Carrie     | Cordero   |
| 4  | Devon      | Dupre     |
| 5  | Carrie     | Eastman   |

-------------------------------
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
- [ ] `model.errors[:address] << "This address is invalid"`

#### Q15. Given the URL helper `product_path(@product)`, which statement would be expected to be _false_?
- [ ] If sent using the PATCH HTTP method, the URL could be used to update a product in the database.
- [ ] If sent using the POST HTTP method, the URL would create a new product in the database.
- [ ] If sent using the GET HTTP method, the URL would execute the show action in ProductsController.
- [ ] If sent using the DELETE HTTP method, the URL would call the destroy action by default.

#### Q16. Given this code, which choice would be expected to be a _true_ statement if the user requests the index action?

```rb
class DocumentsController < ApplicationController
  before_action :require_login
  def index
    @documents = Document.visible.sorted
  end
end
```

- [ ] The user's documents will be loaded.
- [ ] The index action will run normally because `:index` is not listed as an argument to `before_action`.
- [ ] The `require_login` method will automatically log in the user before running the index action.
- [ ] The index action will not be run if the `require_login` method calls render or `redirect_to`.

#### Q17. In Rails, how would you cache a partial template that is rendered?
- [ ] `render partial: ‘shared/menu’, cached: true`
- [ ] `render_with_cache partial: ‘shared/menu’`
- [ ] `render partial: ‘shared/menu’`
- [ ] `render partial: ‘shared/menu’, cached_with_variables: {}`

#### Q18. What is the reason for using Concerns in Rails?
- [ ] Concerns allow modularity and code reuse in models, controllers, and other classes.
- [ ] Concerns are used to separate class methods from models.
- [ ] Concerns are used to increase security of Rails applications.
- [ ] Concerns are used to refactor Rails views.

#### Q19. When using an ActiveRecord model, which method will create the model instance in memory and save it to the database?
- [ ] `build`
- [ ] `new`
- [ ] `create`
- [ ] `save`

#### Q20. You are using an existing database that has a table named `coffee_orders`. What would the ActiveRecord model be named in order to use that table?
- [ ] `CoffeeOrders`
- [ ] `Coffee_Orders`
- [ ] `Coffee_Order`
- [ ] `CoffeeOrder`

#### Q21. In ActiveRecord, what is the difference between the `has_many` and `has_many :through` associations?
- [ ] The `has_many: through` association is the one-to-many equivalent to the `belongs_to` one-to-one association.
- [ ] Both associations are identical, and `has_many: through` is maintained only for legacy purposes.
- [ ] The `has_many` association is a one-to-many association, while `has_many: through` is a one-to-one association that matches through a third model.
- [ ] Both are one-to-many associations but with `has_many :through`, the declaring model can associate through a third model.

#### Q22. How do you add Ruby code inside Rails views and have its result outputted in the HTML file?
- [ ] Create an embedded Ruby file (.html.erb) and surround the Ruby code with `<% %>`.
- [ ] Insert Ruby code inside standard HTML files and surround it with `<% %>`. The web server will handle the rest.
- [ ] Create an embedded Ruby file (.html.erb) and surround the Ruby code with `<%= %>`.
- [ ] Put the code in an .rb file and include it in a `<link>` tag of an HTML file.

#### Q23. How would you render a view using a different layout in an ERB HTML view?
- [ ] `<% render 'view_mobile' %>`
- [ ] `<% render 'view', use_layout: 'mobile' %>`
- [ ] `<% render 'view', layout: 'mobile' %>`
- [ ] `<% render_with_layout 'view', 'mobile' %>`

#### Q24. Given this controller code, which choice describes the expected behavior if parameters are submitted to the update action that includes values for the product's name, style, color, and price?

```rb
class ProductController < ActionController::Base

  def update
    @product = Product.find(params[:id])
    if @product.update_attributes(product_params)
      redirect_to(product_path(@product))
    else
      render('edit')
    end
  end

  private

  def product_params
    params.require(:product).permit(:name, :style, :color)
  end
end
```

- [ ] The product will not be updated and the edit template will be rendered.
- [ ] The product will not be updated and the controller will raise an ActiveModel::ForbiddenAttributes exception.
- [ ] The product will be updated with the values for name, style, and color, but the value for price will be ignored.
- [ ] The product will be updated with the values for name, style, color, and price.

#### Q25. A Rails project has ActiveRecord classes defined for Classroom and Student. If instances of these classes are related so that students are assigned the ID of one particular classroom, which choice shows the correct associations to define?

- [ ] A

```rb
class Classroom < ActiveRecord::Base
  belongs_to :students, class_name: 'Student'
end

class Student < ActiveRecord::Base
  belongs_to :classrooms, class_name: 'Classroom'
end
```

- [ ] B

```rb
class Student < ActiveRecord::Base
  has_many :classrooms, dependent: true
end

class Classroom < ActiveRecord::Base
  has_many :students, dependent: false
end
```

- [ ] C

```rb
class Student < ActiveRecord::Base
  has_many :classrooms
end

class Classroom < ActiveRecord::Base
  belongs_to :student
end
```

- [ ] D

```rb
class Classroom < ActiveRecord::Base
  has_many :students
end

class Student < ActiveRecord::Base
  belongs_to :classroom
end
```

#### Q26. Where should you put images, JavaScript, and CSS so that they get processed by the asset pipeline?

- [ ] app/static
- [ ] app/images
- [ ] app/assets
- [ ] app/views

#### Q27. If the Rails asset pipeline is being used to serve JavaScript files, how would you include a link to one of those JavaScript files in a view?

- [ ] `<script src="/main.js"></script>`
- [ ] `<%= javascript_include_tag 'main' %>`
- [ ] `<%= javascript_tag 'main' %>`
- [ ] `<!-- include_javascript 'main' -->`

#### Q28. In Rails, what caching stores can be used?

- [ ] MemCacheStore, MongoDBStore, MemoryStore, and FileStore
- [ ] MemoryStore, FileStore, and CacheCacheStore
- [ ] MemoryStore, FileStore, MemCacheStore, RedisCacheStore, and NullStore
- [ ] MemoryStore, FileStore, MySQLStore, and RedisCacheStore

#### Q29. What is the correct way to generate a ProductsController with an index action using only the command-line tools bundled with Rails?

- [ ] `rails generate controller --options {name: "Products", actions: "index"}`
- [ ] `rails generate controller --name Products --action index`
- [ ] `rails generate controller Products index`
- [ ] `rails generate ProductsController --actions index`

#### Q30. If a model class is named Product, in which database table will ActiveRecord store and retrieve model instances?

- [ ] `product_table`
- [ ] `all_products`
- [ ] `products_table`
- [ ] `products`

#### Q31. What is a popular alternative template language for generating views in a Rails app that is focused on simple abstracted markup?

- [ ] Mustache
- [ ] Haml
- [ ] Liquid
- [ ] Tilt

#### Q32. When Ruby methods add an exclamation point at the end of their name (such as `sort!`), what does it typically indicate?

- [ ] The method executes using "sudo" privileges.
- [ ] Any ending line return will be omitted from the result.
- [ ] The method will ignore exceptions that occur during execution.
- [ ] It is a more powerful or destructive version of the method.

#### Q33. What part of the code below causes the method `#decrypt_data` to be run?

```rb
class MyModel < ApplicationRecord
after_find :decrypt_data
end
```

- [ ] `MyModel.first.update(field: 'example')`
- [ ] `MyModel.where(id: 42)`
- [ ] `MyModel.first.destroy`
- [ ] `MyModel.new(field: 'new instance')`

#### Q34. Which Rails helper would you use in the application view to protect against CSRF (Cross-Site Request Forgery) attacks?

- [ ] `csrf_protection`
- [ ] `csrf_helper`
- [ ] `csrf_meta_tags`
- [ ] `csrf`

#### Q35. In the model `User` you have the code shown below. When saving the model and `model.is_admin` is set to true, which callback will be called?

```rb
before_save :encrypt_data, unless: ->(model) { model.is_admin }
after_save :clear_cache, if: ->(model) { model.is_admin }
before_destroy :notify_admin_users, if: ->(model) { model.is_admin }
```

- [ ] `encrypt_data`
- [ ] `clear_cache`
- [ ] `notify_admin_users`
- [ ] None of these callbacks will be called when `is_admin` is true.

#### Q36. In a Rails controller, what does the code `params.permit(:name, :sku)` do?

- [ ] It filters out all parameters.
- [ ] It filters out submitted form parameters that are not named `:name` or `:sku` to make forms more secure.
- [ ] It raises an error if parameters that are not named `:name` or `:sku` are found.
- [ ] It raises an error if the `:name` and `:sku` parameters are set to `nil`.

#### Q37. Review the code below. Which Ruby operator should be used to fill in the blank so that the `sort` method executes properly?

```rb
[5,8,2,6,1,3].sort {|v1,v2| v1 ___ v2}
```

- [ ] `=>`
- [ ] `<==>`
- [ ] `<=>`
- [ ] `||`
