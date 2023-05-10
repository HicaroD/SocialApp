create schema if not exists socialapp_database;

create table if not exists socialapp_database.users(
  name varchar(50) not null,
  username varchar(10) primary key,
  email varchar(30) not null,
  is_verified boolean not null
);

create table if not exists socialapp_database.post(
  id serial primary key,
  user_username_fk varchar(10) not null references socialapp_database.users(username) on delete cascade
);

create table if not exists socialapp_database.textpost(
  post_id_fk integer not null references socialapp_database.post(id) on delete cascade,
  text text not null,
  primary key (post_id_fk)
);

create table if not exists socialapp_database.videopost(
  post_id_fk integer not null references socialapp_database.post(id) on delete cascade,
  video bytea not null,
  primary key (post_id_fk)
);

create table if not exists socialapp_database.photopost(
  post_id_fk integer not null references socialapp_database.post(id) on delete cascade,
  photo bytea not null,
  primary key (post_id_fk)
);

create table if not exists socialapp_database.comment(
  id serial primary key,
  text text not null
);

create table if not exists socialapp_database.send(
  post_id_fk integer not null references socialapp_database.post(id) on delete cascade,
  comment_id_fk integer not null references socialapp_database.comment(id) on delete cascade,
  user_username_fk varchar(10) not null references socialapp_database.users(username) on delete cascade,
  primary key (comment_id_fk)
);
