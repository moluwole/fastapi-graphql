from orator.migrations import Migration


class CreateCommentsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('comments') as table:
            table.increments('id')
            table.integer('user_id').unsigned().nullable()
            table.foreign('user_id').references('id').on('users')
            table.integer('post_id').unsigned().nullable()
            table.foreign('post_id').references('id').on('posts')
            table.text('body')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('comments')
