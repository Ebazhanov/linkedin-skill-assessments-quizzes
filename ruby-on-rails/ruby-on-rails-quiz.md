## Ruby on Rails

#### Q1. When rendering a partial in a view, how would you pass local variables for rendering?

- [ ] `<%= render partial: "nav", selected: "about"}%>`
- [ ] `<%= render partial: "nav", local_variables: {selected: "about"} %>`
- [x] `<%= render partial: "nav", locals: {selected: "about"}`

#### Q2. Within a Rails controller, which code will prevent the parent controller's before_action `:get_feature` from running?

- [x] `skip_before_action :get_feature`
- [ ] `skip :get_feature, except: []`
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

- [x] `ActiveSupport::Concern`
- [ ] `RailsHelper.CommonClass`
- [ ] `ActiveJob::Mixin`
- [ ] `ActiveSupport::Module`

#### Q6. In Rails, which code would you use to define a route that handles both the `PUT` and `PATCH` `REST HTTP` verbs?

- [ ] `put :items, include: patch`
- [ ] `put 'items', to: 'items#update'`
- [x] `match 'items', to 'items#update', via: [:put, :patch]`
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
- [x] It would include columns for `:documentable_id` and `:documentable_type`.
- [ ] It would include columns for `:documentable` and `:type`.
- [ ] It would include a column for `:polymorphic_type`.

#### Q10. Are instance variables set within a controller method accessible within a view?

- [x] Yes, any instance variables that are set in an action method on a controller can be accessed and displayed in a view.
- [ ] Yes, instance variables set within an action method are accessible within a view, but only when render is explicitly called inside the action method.
- [ ] No, instance variables in a controller are private and are not accessible.
- [ ] No, instance variables can never be set in a controller action method.

#### Q11. When a validation of a field in a Rails model fails, where are the messages for validation errors stored?

- [x] `my_model.errors[:field]`
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
- [x] `model.errors[:address] << "This address is invalid"` [Reference: Custom Validator](https://guides.rubyonrails.org/v5.2/active_record_validations.html#custom-validators)

#### Q15. Given the URL helper `product_path(@product)`, which statement would be expected to be _false_?

- [ ] If sent using the PATCH HTTP method, the URL could be used to update a product in the database.
- [x] If sent using the POST HTTP method, the URL would create a new product in the database.
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
- [x] The index action will not be run if the `require_login` method calls render or `redirect_to`.

#### Q17. In Rails, how would you cache a partial template that is rendered?

- [x] `render partial: ‘shared/menu’, cached: true`
- [ ] `render_with_cache partial: ‘shared/menu’`
- [ ] `render partial: ‘shared/menu’`
- [ ] `render partial: ‘shared/menu’, cached_with_variables: {}`

#### Q18. What is the reason for using Concerns in Rails?

- [x] Concerns allow modularity and code reuse in models, controllers, and other classes.
- [ ] Concerns are used to separate class methods from models.
- [ ] Concerns are used to increase security of Rails applications.
- [ ] Concerns are used to refactor Rails views.

#### Q19. When using an ActiveRecord model, which method will create the model instance in memory and save it to the database?

- [ ] `build`
- [ ] `new`
- [x] `create` [Reference](https://medium.com/@de.usmanusa/difference-between-create-new-and-save-methods-in-activerecord-ea135085a08c)
- [ ] `save`

#### Q20. You are using an existing database that has a table named `coffee_orders`. What would the ActiveRecord model be named in order to use that table?

- [ ] `CoffeeOrders`
- [ ] `Coffee_Orders`
- [ ] `Coffee_Order`
- [x] `CoffeeOrder` [Reference](https://guides.rubyonrails.org/active_record_basics.html#naming-conventions)

#### Q21. In ActiveRecord, what is the difference between the `has_many` and `has_many :through` associations?

- [ ] The `has_many: through` association is the one-to-many equivalent to the `belongs_to` one-to-one association.
- [ ] Both associations are identical, and `has_many: through` is maintained only for legacy purposes.
- [ ] The `has_many` association is a one-to-many association, while `has_many: through` is a one-to-one association that matches through a third model.
- [x] Both are one-to-many associations but with `has_many :through`, the declaring model can associate through a third model.

#### Q22. How do you add Ruby code inside Rails views and have its result outputted in the HTML file?

- [x] Create an embedded Ruby file (.html.erb) and surround the Ruby code with `<% %>`.
- [ ] Insert Ruby code inside standard HTML files and surround it with `<% %>`. The web server will handle the rest.
- [ ] Create an embedded Ruby file (.html.erb) and surround the Ruby code with `<%= %>`.
- [ ] Put the code in an .rb file and include it in a `<link>` tag of an HTML file.

#### Q23. How would you render a view using a different layout in an ERB HTML view?

- [ ] `<% render 'view_mobile' %>`
- [ ] `<% render 'view', use_layout: 'mobile' %>`
- [x] `<% render 'view', layout: 'mobile' %>` [Reference](https://stackoverflow.com/a/19277971)
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
- [x] The product will not be updated and the controller will raise an ActiveModel::ForbiddenAttributes exception.
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

- [x] D

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
- [x] app/assets [Reference: RoR folder structure](https://images.app.goo.gl/CfKZPEQcGExfSx5C6)
- [ ] app/views

#### Q27. If the Rails asset pipeline is being used to serve JavaScript files, how would you include a link to one of those JavaScript files in a view?

- [ ] `<script src="/main.js"></script>`
- [x] `<%= javascript_include_tag 'main' %>`
- [ ] `<%= javascript_tag 'main' %>`
- [ ] `<!-- include_javascript 'main' -->`

#### Q28. In Rails, what caching stores can be used?

- [ ] MemCacheStore, MongoDBStore, MemoryStore, and FileStore
- [ ] MemoryStore, FileStore, and CacheCacheStore
- [x] MemoryStore, FileStore, MemCacheStore, RedisCacheStore, and NullStore
- [ ] MemoryStore, FileStore, MySQLStore, and RedisCacheStore

#### Q29. What is the correct way to generate a ProductsController with an index action using only the command-line tools bundled with Rails?

- [ ] `rails generate controller --options {name: "Products", actions: "index"}`
- [ ] `rails generate controller --name Products --action index`
- [x] `rails generate controller Products index`
- [ ] `rails generate ProductsController --actions index`

#### Q30. If a model class is named Product, in which database table will ActiveRecord store and retrieve model instances?

- [ ] `product_table`
- [ ] `all_products`
- [ ] `products_table`
- [x] `products`

#### Q31. What is a popular alternative template language for generating views in a Rails app that is focused on simple abstracted markup?

- [ ] Mustache
- [x] Haml [Reference](https://medium.com/@bretcameron/so-you-think-you-know-html-7813c03f8ff6)
- [ ] Liquid
- [ ] Tilt

#### Q32. When Ruby methods add an exclamation point at the end of their name (such as `sort!`), what does it typically indicate?

- [ ] The method executes using "sudo" privileges.
- [ ] Any ending line return will be omitted from the result.
- [ ] The method will ignore exceptions that occur during execution.
- [x] It is a more powerful or destructive version of the method.

#### Q33. What part of the code below causes the method `#decrypt_data` to be run?

```rb
class MyModel < ApplicationRecord
after_find :decrypt_data
end
```

- [ ] `MyModel.first.update(field: 'example')`
- [x] `MyModel.where(id: 42)`
- [ ] `MyModel.first.destroy`
- [ ] `MyModel.new(field: 'new instance')`

#### Q34. Which Rails helper would you use in the application view to protect against CSRF (Cross-Site Request Forgery) attacks?

- [ ] `csrf_protection`
- [ ] `csrf_helper`
- [x] `csrf_meta_tags` [Reference](https://api.rubyonrails.org/classes/ActionView/Helpers/CsrfHelper.html)
- [ ] `csrf`

#### Q35. In the model `User` you have the code shown below. When saving the model and `model.is_admin` is set to true, which callback will be called?

```rb
before_save :encrypt_data, unless: ->(model) { model.is_admin }
after_save :clear_cache, if: ->(model) { model.is_admin }
before_destroy :notify_admin_users, if: ->(model) { model.is_admin }
```

- [x] `encrypt_data`
- [ ] `clear_cache`
- [ ] `notify_admin_users`
- [ ] None of these callbacks will be called when `is_admin` is true.

#### Q36. In a Rails controller, what does the code `params.permit(:name, :sku)` do?

- [ ] It filters out all parameters.
- [x] It filters out submitted form parameters that are not named `:name` or `:sku` to make forms more secure.
- [ ] It raises an error if parameters that are not named `:name` or `:sku` are found.
- [ ] It raises an error if the `:name` and `:sku` parameters are set to `nil`.

#### Q37. Review the code below. Which Ruby operator should be used to fill in the blank so that the `sort` method executes properly?

```rb
[5,8,2,6,1,3].sort {|v1,v2| v1 ___ v2}
```

- [ ] `=>`
- [ ] `<==>`
- [x] `<=>`
- [ ] `||`

#### Q38. Which ActiveRecord query prevents SQL injection?

- [ ] `Product.where("name = " << @keyword)`
- [ ] `Product.where("name = " + h(@keyword))`
- [ ] `Product.where("name = ?", @keyword)`
- [x] `Product.where("name = #{@keyword}")`

#### Q39. You made a spelling mistake while creating a table for bank accounts. Which code would you expect to see in a migration to fix the error?

- [x] A

```
class IAmADummy < ActiveRecord::Migration
  def change
    rename_column :accounts, :account_hodler, :account_holder
  end
end
```

- [ ] B

```
class FixSpellling < ActiveRecord::Migration
  def change
    rename :accounts, :account_hodler, :account_holder
  end
end
```

- [ ] C

```
class CoffeeNeeded < ActiveRecord::Migration
  def change
    remove_column :accounts, :account_hodler
    add_column :accounts, :account_holder
  end
end
```

- [ ] D

```
class OopsIDidItAgain < ActiveRecord::Migration
  def rename
    :accounts, :account_hodler, :account_holder
  end
end
```

#### Q40. Which HTML is closes to what this code would output?

```
<% check_box(:post, :visible) %>
```

- [x] A

```
<input type="hidden" name="post[visible]" value="0" />
<input type="checkbox" name="post[visible]" value="1" />
```

- [ ] B

```
<checkbox name="post[visible]" value="1" />
```

- [ ] C

```
<input type="checkbox" name="post[visible]" value="1" data-default-value="0" />
```

- [ ] D

```
<input type="checkbox" name="post[visible]" value="1" />
```

#### Q41. There is a bug in this code. The logout message is not appearing on the login template. What is the cause?

```
class AccessController < ActionController::Base
  def destroy
    session[:admin_id] = nil
    flash[:notice] = ""You have been logged out""
    render('login')
end
```

- [x] The string assigned to flash[:notice] will not be available until the next browser request.
- [ ] An instance variable should be used for flash[:notice]
- [ ] This is an invalid syntax to use to assign valuse to flash[:notice]
- [ ] The previous value of flash[:notice] will not be cleared automatically

#### Q42. Which statement about ActiveRecord models is true?

- [ ] Each database column requres adding a matching attr_accessor declaration in the ActiveRecord model.
- [ ] All attributes in an ActiveRecord model are read-only declared as writable using attr_accessible
- [x] An instance of an ActiveRecord model will have attributes that match the columns in a corresponding database table.
- [ ] ActiveRecord models can have only attributes that have a matching database column

#### Q43. What is the correct way to assign a value to the session?

- [ ] A

```
$_SESSION['user_id'] = user.id
```

- [ ] B

```
@session ||= Session.new << user.id
```

- [ ] C

```
session_save(:user_id, user.id)
```

- [x] D

```
session[:user_id] = user.id
```

#### Q43. Which choice best describes the expected value of @result?

```
@result = Article.first.tags.build(name: 'Urgent')
```

- [ ] either true or false
- [x] an unsaved Tag instance
- [ ] a saved Tag instance
- [ ] an array of Tag instances

#### Q44. What is the correct syntax for inserting a dynamic title tag into the header of your page from within an ERB view template?

- [ ] A

```
<% render :head do %>
  <title>My page title</title>
<% end %>
```

- [ ] B

```
<% content_for :head do %>
  <title>My page title</title>
<% end %>
```

- [x] C

```
<% render "shared/head, locals: {title: "My page title"} %>
```

- [ ] D

```
<% tield :head do %>
  <title>My page title</title>
<% end %>
```

#### Q45. How would you validate that a project's name is not blank, is fewer than 50 characters, and is unique?

- [x] A

```
class Project
  validates :name, presence: true, length: { maximum: 50 }, uniqueness: true
end
```

- [ ] B

```
class Project
  validate_attribute :name, [:presence, :uniqueness], :length => 1..50
end
```

- [ ] C

```
class Project
  validate_before_save :name, [:presence, [:length, 50], :uniqueness], :length => 1..50
end
```

- [ ] D

```
class Project
  validates_presense_of :name, :unique => true
  validates_length_of :name, :maximum => 50
end
```

#### Q46. If a product has a user-uploadable photo, which ActiveStorage method should fill in the blank?

```
class Product << ApplicationRecord
  ____ :photo
end

```

- [x] has_one_attached
- [ ] has_image
- [ ] attached_file
- [ ] acts_as_attachment

#### Q47. If the only route defined is resources :products, what is an example of a URL that could be generated by this link_to method?

```
link_to('Link', {controller: 'products', action: 'index', page: 3})
```

- [x] A

```
/products?page=3
```

- [ ] B

```
/products/index/3
```

- [ ] C

```
/products/page/3
```

- [ ] D

```
/products/index/page/3
```

#### Q48. Which part of the Rails framework is primarily responsible for making decisions about how to respond to a browser request?

- [ ] view
- [x] controller
- [ ] ActiveRecord
- [ ] model

#### Q49. If User is an ActiveRecord class, which choice would be expected to return an array?

- [x] User.where(last_name: 'Smith')
- [ ] User.find_or_create(last_name: 'Smith')
- [ ] User.find_by_last_name('Smith')
- [ ] User.find('Smith')

#### Q50. Which choice is not a valid Rails route?

- [x] route "products/index", to: "products/index", via: :get
- [ ] match "products/index", to: "products#index", via: :get
- [ ] root "products/index"
- [ ] get "products/index"

#### Q51. Given a table of blog_posts and a related table of comments (comments made on each blog post), which ActiveRecord query will retrieve all blog posts with comments created during @range?

- [x] BlogPost.joins (:comments).where(comments: {created_at: @range})
- [ ] BlogPost.where(['comments.created_at', @range])
- [ ] BlogPost.preload ("comments.created_at").where(created_at: @range)
- [ ] BlogPost.includes (:comments).where('comments.created_at' => @range)

#### Q52. Given this Category model with an attribute for "name", what code would fill in the blank so that it sets saved_name to a string that is the category name that existed before the name was changed?

```ruby
class Category < ActiveRecord::Base
  # has a database column for :name
end

category = Category.first
category.name = 'News'
saved_name = _____
```

- [ ] category.name_was
- [ ] category.saved(:name)
- [x] category.changes[:name]
- [ ] category.name_changed?

#### Q53. Given two models, what is the issue with the query used to fetch them?

```ruby
class LineItem < ApplicationRecord
end

class Order < ApplicationRecord
  has_many :line_items
end

Order.limit(3).each { |order| puts order.line_items }
```

- [ ] This query will result in extensive caching, and you will have to then deal with caching issues.
- [x] This query will result in the N+1 query issue. Three orders will result in four queries.
- [ ] This query will result in the 1 query issue. Three orders will result in one query.
- [ ] There are no issues with this query, and you are correctly limiting the number of Order models that will be loaded.

#### Q54. Which choice is an *incorrect* way to render a partial?

- [ ] `<%= render(:partial => 'shared/product') %>`
- [ ] `<%= render('shared/product', :collection => @products) %>`
- [x] `<%= render(template: 'shared/product', with: @products) %>`
- [ ] `<%= render('shared/product', locals: { product: @product }) %>`

#### Q55. Which code sample will skip running the `login_required` "before" filter on the `get_posts` controller action?

- [ ] `before_action :login_required, skip: [:get_posts]`
- [ ] `skip_before_action :login_required, except: [:get_posts]`
- [x] `skip_before_action :login_required, only: [:get_posts]`
- [ ] `skip_action before: :login_required, only: [:get_posts]`

#### Q56. Within a Rails model with a `cache_key` method, which code snippet will expire the cache whenever the model is updated?

- [ ] A

```ruby
after_update_commit do
destroy
end
```

- [ ] B

```ruby
after_destroy do
Rails.cache.delete(cache_key)
end
```

- [ ] C

```ruby
after_update_commit do
Rails.cache.delete(cache_key)
end
```

- [x] D

```ruby
after_update_commit do
Rails.cache.destroy(cache_key)
end
```

#### Q57. After this migration has been executed, which statement would be true?

```ruby
class CreateGalleries < ActiveRecord::Migration
  def change
    create_table :galleries do |t|
      t.string :name, :bg_color
      t.integer :position
      t.boolean :visible, default: false
      t.timestamps
    end
  end
end
```

- [ ] The galleries table will have no primary key.
- [x] The galleries table will include a column named "updated_at".
- [ ] The galleries table will contain exactly seven columns.
- [ ] The galleries table will have an index on the position column.

#### Q58. Which code would you add to return a 404 to the API caller if the user is not found in the database?

```ruby
class UsersController < ApplicationController
  def show
    @user = User.find(params[:id])
    render json: @user, status: :ok,
    # Missing code
end
```

- [ ] A

```ruby
rescue => e
  logger.info e
end
```

- [x] B

```ruby
rescue_from ActiveRecord::RecordNotFound, with: :render_not_found_response
```

- [ ] C

```ruby
rescue ActiveRecord::RecordNotFound
  render json: { message: 'User not found' }, status: :not_found
end
```

- [ ] D

```ruby
raise ActiveRecord::RecordNotFound
  render json: { message: 'User not found' }, status: :user_not_found
end
```
