# -*- coding: utf-8 -*-
# @file 	TwitterAccessor.rb
# @author 	Masakaze Sato
# 
# @brief 	Twitterへのアクセサ

require 'rubygems'
require 'twitter'
require 'yaml'

include Twitter

module Twitter

ENV["SSL_CERT_FILE"] = "#{File.dirname(__FILE__)}/cacert.pem"

#
# Tweet情報
#
class TweetInfo

  attr_accessor :text, :screen_name, :name, :id

  def initialize()
    @text = nil
    @screen_name = nil
    @name = nil
    @id = nil
  end

  #
  # Twitter::Tweetクラスから情報作成
  #
  def create_from_tweet_class(tweet)
    @text = tweet.text
    @screen_name = tweet.user.screen_name
    @name = tweet.user.name
    @id = tweet.id
  end

  #
  # search関数の返り値から(Hash)
  #
  def create_from_search_result(tweet)
    @text = tweet[:text]
    @screen_name = tweet[:user][:screen_name]
    @name = tweet[:user][:name]
  end

end # class Twitter Info

#
# Twitterのアクセサ
#
class TwitterAccessor

  def initialize()
    @client = nil
  end

#
# 初期化
#

  #
  # ログイン
  #
  def login(consumer_key, consumer_secret, oauth_token, oauth_token_secret)
    @client = Twitter::REST::Client.new { |config|
      config.consumer_key = consumer_key
      config.consumer_secret = consumer_secret
      config.access_token = oauth_token
      config.access_token_secret = oauth_token_secret
    }
  end

  #
  # ログイン
  #
  def login_from_file(user_log_info_yaml)
    user_log_info = YAML.load_documents(File.open(user_log_info_yaml).read())[0]
    login(user_log_info["ConsumerKey"],
          user_log_info["ConsumerKeySecret"],
          user_log_info["AccessToken"],
          user_log_info["AccessTokenSecret"])
  end

#
#
#
  def get_client()
    if @client == nil
      puts "TwitterAccessor::Loginを実行してください"
      exit 1
    end

    return @client
  end
end # class TwitterAccessor
  
module TwitterUtil

  #
  # フレンド数
  #
  def login(user_info_yaml)
    accessor = TwitterAccessor.new()
    accessor.login_from_file(user_info_yaml)
    return accessor
  end
  module_function :login

	#
	# ユーザー情報取得
	#
  def get_user(accessor)
    client = accessor.get_client()
    return accessor.get_client().user
  end

  #
  # フレンド数
  #
  def get_friends_count(accessor)
    return get_user(accessor).friends_count
  end

  #
  # フォローワー数取得
  #
  def get_followers_count(accessor)
    return get_user(accessor).followers_count
  end

  #
  # ツイート数
  #
  def get_tweets_count(accessor)
    return get_user(accessor).tweets_count
  end

  #
  # ホームタイムライン取得
  #
  def get_home_timelines(accessor)
    result = accessor.get_client().home_timeline()
    tweets = Array.new()
    result.each { |tweet|
      info = TweetInfo.new()
      info.create_from_tweet_class(tweet)
      tweets << info
    }
    return tweets
  end

  #
  # 投稿
  #
  def post(accessor, text, post_options = {})
    return accessor.get_client().update(text, post_options)
  end
  module_function :post
  
  #
  #
  #
  def post_with_media(accessor, text, img_path)
    accessor.get_client.update_with_media(text, open(img_path))
  end
  module_function :post_with_media

  #
  #
  #
  def get_user_timelines(accessor, user_name)
    return accessor.get_client().user_timeline(user_name)
  end

  #
  # 検索
  #
  def search_tweets_from_keyword(accessor, keyword)
    result = accessor.get_client().search(keyword, :result_type => "recent", :count => 20).to_h[:statuses]
    tweets = Array.new()
    result.each { |tweet|
      info = TweetInfo.new()
      info.create_from_search_result(tweet)
      tweets << info
    }
    return tweets
  end

#
# TweetInfoから特定の情報を抽出
#
  #
  # 宛先をユーザー名を取得
  #
  def get_to_user(info)
    text = info.text
    /#{TWITTER_TO_REX}.*/ =~ text
    to_array = $1.split(/\s+/).select { |to| to.slice!(0) }
    return to_array
  end

  #
  # URLを抽出
  #
  def extract_url(info)
    text = info.text
    url_array = text.scan(/#{TWITTER_URL_REX}/)
    return url_array
  end

end # module TwitterUtil

end # module Twitter

if __FILE__ == $0

	if ARGV.length == 0
		accessor = TwitterUtil.login(File.join(File.dirname(__FILE__), "TwitterUserInfo.yaml"))
  
		TwitterUtil.post_with_media(accessor, "画像投稿Utilテスト", "/Users/Masakaze/home/GitProject/ProjectSalieri/Python/EyeSensor/SampleImage/Apple.jpg")
		exit 0
	end
	
	require 'optparse'
	exec_opt = {}
	opt = OptionParser.new { |opt|
		opt.on("--post_text=Text", "投稿テキスト"){ |v| exec_opt[:post_text] = v }
		opt.on("--image_path=ImagePath", "投稿画像パス"){ |v| exec_opt[:img_path] = v }
		opt.on("--help", "ヘルプ") { 
			puts opt.help
			exit 0
		}
	}
	
	begin
		opt.parse!(ARGV)
	rescue => e
		puts e.message
		puts opt.help
		exit 1
	end
	
	p exec_opt
	
	accessor = TwitterUtil.login(File.join(File.dirname(__FILE__), "TwitterUserInfo.yaml"))
  
  	if exec_opt[:img_path] != nil
		TwitterUtil.post_with_media(accessor, exec_opt[:post_text], exec_opt[:img_path])
	else
		TwitterUtil.post(accessor, exec_opt[:post_text])
	end

end
