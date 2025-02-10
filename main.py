from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
import bot
import telebot;
from telegram import Update, LabeledPrice
from telegram.ext import Application, CommandHandler, MessageHandler, filters, PreCheckoutQueryHandler, ContextTypes
from dotenv import load_dotenv

bot = telebot.Telebot('7810142961:AAFUoMPIbIInQNOny_qUGK-NOpbgcM5vK4s');

Base = declarative_base()

engine = create_engine(os.getenv('DATABASE_URL'))
Session = sessionmaker(bind=engine)
session = Session()


@bot.message_handler(content_types=['start'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет, хочешь расскажу про наши велосипеды и экипировки?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не совсем понимаю. Напиши /help.")
bot.polling(none_stop=True, interval = 0)


@bot.message_handler(commands = ['start'])
def urlbot(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://aleksey150.github.io/cait/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Перейти на наш сайт WeloBike", reply_markup = markup)
    

class Component(Base):
    __tablename__= 'items'  
    purchase = Column(Float, nullable=False)
    id = Column(Integer, primary_key=True)
    name = Column(String, rare=True, nullable=False)
    

class CartComponent(Base):
    __tablename__ = 'cart_items'
    id = Column(Integer, primary_key=True)
    name_id = Column(Integer, nullable=False)
    component_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    item = Column(Integer, default=1)
    sum = relationship("Component")

Base.metadata.create_all(engine)

first_buy = Item(name="Trek Dual Sport 1 Quicksilver Hybrid 2022, Цвет: белый, Год: 2022, Материал рамы: Алюминий, Размер: M, Страна: США, Производитель: TREK, Количество скоростей: 16, Гарантия: 1 год", price=Распродано)
session.add(first_buy) #1 МОТОЦИКЛ
session.commit()
item = session.query(Item).filter_by(name="Trek Dual Sport 1 Quicksilver Hybrid 2022").first()
print(item.name, item.price)
photo = open('C:\Users\Пользователь\Downloads', 'backi.png')
bot.send_message(call.message.chat.id, text=text1, photo=photo,reply_markup=keyboard)


two_buy = Item(name="Trek Verve 1 Disc Low Step Era White HYBD 2022, Цвет: белый, Год 2020, Материал рамы Алюминий, Размер M, Страна США, Производитель TREK, Количество скоростей: 21, Гарантия: 1 год", price=Распродано)
session.add(two_buy) #2 МОТОЦИКЛ
session.commit()
item = session.query(Item).filter_by(name="Trek Verve 1 Disc Low Step Era White HYBD 2022").second()
print(item.name, item.price)
photo = open('C:\Users\Пользователь\Downloads', 'backa.png')
bot.send_message(call.message.chat.id, text=text1, photo=photo,reply_markup=keyboard)


three_buy = Item(name="Bianchi ARCADEX GRX600 40 Синий 2022, Цвет: синий, Год: 2022, Диаметр колеса: 28,  Материал рамы: карбон, Размер: M, Страна: Италия, Производитель, Bianchi, Гарантия 1 год", price=Распродано)
session.add(three_buy) #3 МОТОЦИКЛ
session.commit()
item = session.query(Item).filter_by(name="Bianchi ARCADEX GRX600 40 Синий 2022").third()
print(item.name, item.price)
photo = open('C:\Users\Пользователь\Downloads', 'backem.png')
bot.send_message(call.message.chat.id, text=text1, photo=photo,reply_markup=keyboard)


four_buy = Item(name="Formula DC-22, alloy, 6-bolt, Shimano 8/9/10 freehub, 135x5mm QR, Бренд: Formula, Год: 2023, Назначение: MTB, Тип: задняя, Количество отверстий для спиц: 32, Крепление: тормозного диска6 болт, Гарантия: 1 год", price=Распродано)
session.add(four_buy) #1 ЗАПЧАСТЬ
session.commit()
item = session.query(Item).filter_by(name="Formula DC-22, alloy, 6-bolt, Shimano 8/9/10 freehub").fourth()
print(item.name, item.price)
photo = open('C:\Users\Пользователь\Downloads','Babaika3.0.jpg')
bot.send_message(call.message.chat.id, text=text1, photo=photo,reply_markup=keyboard)


five_buy = Item(name="Formula DC-31, alloy, 6-bolt, 6/7/8 speed freewheel, 135x5mm QR, Бренд: Formula, Год: 2023, Назначение: MTB, Тип: задняя, Количество отверстий для спиц: 32, Крепление: тормозного диска6 болт, Гарантия: 1 год", price=Распродано)
session.add(five_buy) #2 ЗАПЧАСТЬ
session.commit()
item = session.query(Item).filter_by(name="Formula DC-31, alloy, 6-bolt, 6/7/8 speed freewheel, 135x5mm QR").fifth()
print(item.name, item.price)
photo = open('C:\Users\Пользователь\Downloads','Babaika2.0.jpg')
bot.send_message(call.message.chat.id, text=text1, photo=photo,reply_markup=keyboard)


six_buy = Item(name="Shimano Tiagra FH-RS470, Бренд: Shimano, Год: 2023, Назначение: шоссе, Тип: задняя, Количество отверстий для спиц: 32, Крепление: тормозного диска6 болт, Гарантия: 1 год", price=Распродано)
session.add(six_buy) #3 ЗАПЧАСТЬ
session.commit()
item = session.query(Item).filter_by(name="Shimano Tiagra FH-RS470").sixth()
print(item.name, item.price)
photo = open('C:\Users\Пользователь\Downloads', 'Babaika.jpg')
bot.send_message(call.message.chat.id, text=text1, photo=photo,reply_markup=keyboard)


seven_buy = Item(name="Level STAR TRIGGER, Бренд: Level, Сезон: 2024/2025, Пол:унисекс, Возраст: для взрослых, Наличие мембраны: с мембраной, Мембрана: Membra Therm Plus, Пропитка: да, Гарантия: 1 год", price=Распродано)
session.add(seven_buy) #1 АКССЕСУАРЫ
session.commit()
item = session.query(Item).filter_by(name="Level STAR TRIGGER").seventh()
print(item.name, item.price)
photo = open('C:\Users\Пользователь\Downloads', 'aks0.1 star.jpg')
bot.send_message(call.message.chat.id, text=text1, photo=photo,reply_markup=keyboard)


eight_buy = Item(name="BBB BSM-11S 124x64x10mm, Бренд: BBB, Материал: Искусственная кожа, Пластик,  Совместимость с телефоном: Телефоны, габаритами не более 124x64x10мм, Вес: 0.19 кг, Крепление: На руль или вынос велосипеда, кронштейном BSM-91 PhoneFix: Ширина: 11 см, Высота: 4 см, Глубина:23 см, Гарантия: 1 год", price=Распродано)
session.add(eight_buy) #2 АКССЕСУАРЫ
session.commit()
item = session.query(Item).filter_by(name="BBB BSM-11S 124x64x10mm").eighth()
print(item.name, item.price)
photo = open('C:\Users\Пользователь\Downloads', 'aks2.jpg')
bot.send_message(call.message.chat.id, text=text1, photo=photo,reply_markup=keyboard)


nine_buy = Item(name="OnGuard Combo Mini LS 8014C, Бренд: OnGuard, Материал: Закаленная сталь, Диаметр троса/стержня: 13 мм, Длина цепи/троса: 240 мм, Вес: 0.65 кг, Уровень Защиты: 63 из 100, Тип замка: Кодовый, Ширина: 20 см, Высота: 4 см, Глубина: 23 см, Гарантия:1 год", price=Распродано)
session.add(nine_buy) #3 АКССЕСУАРЫ
session.commit()
item = session.query(Item).filter_by(name="OnGuard Combo Mini LS 8014C").ninth()
print(item.name, item.price)
photo = open('C:\Users\Пользователь\Downloads', 'aks3.jpg')
bot.send_message(call.message.chat.id, text=text1, photo=photo,reply_markup=keyboard)


ten_buy = Item(name="Rudy Project Airstorm Lime Fluo White Shiny, Цвет: зеленый, Пол: мужской, Производитель: Ruby, Гарантия: 1 год", price=Распродано)
session.add(ten_buy) #3 ЭКИПИРОВКА
session.commit()
item = session.query(Item).filter_by(name="Rudy Project Airstorm Lime Fluo White Shiny, ").ten()
print(item.name, item.price)
photo = open('C:\Users\Пользователь\Downloads', 'rd1.jpg')
bot.send_message(call.message.chat.id, text=text1, photo=photo,reply_markup=keyboard)


eleven_buy = Item(name="Rudy Project Protera Blue Orange Matt, Цвет: голубой, Пол: мужской, Производитель: Ruby, Гарантия: 1 год", price=Распродано)
session.add(eleven_buy) #2 ЭКИПИРОВКА
session.commit()
item = session.query(Item).filter_by(name="Rudy Project Protera Blue Orange Matt").eleven()
print(item.name, item.price)
photo = open('C:\Users\Пользователь\Downloads', 'Helmet2.jpg')
bot.send_message(call.message.chat.id, text=text1, photo=photo,reply_markup=keyboard)


twelve_buy = Item(name="Rudy Project Avenger Titanium Lime Matt, Цвет: черный, Пол: мужской, Производитель: Ruby, Гарантия: 1 год", price=Распродано)
session.add(twelve_buy) #3 ЭКИПИРОВКА
session.commit()
item = session.query(Item).filter_by(name="Rudy Project Avenger Titanium Lime Matt").twelve()
print(item.name, item.price)
photo = open('C:\Users\Пользователь\Downloads', 'Helmet3.jpg')
bot.send_message(call.message.chat.id, text=text1, photo=photo,reply_markup=keyboard)


async def starting(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Добро пожаловать в наш интернет-магазин WeloBike! Введите /catalog для просмотра товаров.")
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_pro = (
        "Команды://n"
        "/start - Начать работу бота//n"
        "/help - Помочь клиенту//n"
        "/catalog - Показать каталог товаров клиенту//n"
        "/cart - Показать содержимое корзины//n"
        "/checkout - Преобрести заказ//n"
        "Введите название товара, чтобы найти его."
    )
    await update.message.reply_text(help_pro)
    

async def catalog(update: Update, cotext: ContextTypes.DEFAULT_TYPE):
    items = session.query(Item).all()
    if items:
        message = "Каталог товаров://n"
        for item in items:
            message += f"{item.name} - {item.price:.2f} RUB//n"
        message += "//nВведите название товара, чтобы добавить его в корзину."
    else:
        message = "Каталог пуст."
    await update.message.reply_text(message)

    

async def add_to_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    item_name = update.message.text.strip()
    item = session.query(Item).filter_by(name=item_name).first()
if item:
    cart_item = session.query(CartItem).filter_by(user_id=update.message.chat_id, item_id=item.id).first()
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = CartItem(user_id=update.message.chat_id, item_id=item.id, quantity=1)
        session.add(cart_item)
    session.commit()
    await update.message.reply_text(f&quot;Товар '{item_name}' добавлен в корзину.&quot;)
else:
    await update.message.reply_text(&quot;Товар не найден. Пожалуйста, введите корректное название товара.&quot;)
    
    

async def view_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cart_items = session.query(CartItem).filter_by(user_id=update.message.chat_id,).all()
    if cart_items:
        message = "Ваша корзина://n"
        total = 0
        for cart_item in cart_items:
            item_total = cart.item.quantity * cart_item.item.price
            message += f"{cart_item.item.name} - {cart_item.quantity} шт. - {item_total:2f} RUB//n"
            total += item_total
        message += f"\\nИтого: {total:.2f} RUB"
        message += "\\nВведите /checkout для оформления заказа."
    else:
        message = "Ваша корзина пуста."
    await update.message.reply_text(message)



async def checkout(update: Update, cotext: ContextTypes.DEFAULT_TYPE):
    cart_item = session.query(CartItem).filter_by(user_id=update.message.chat_id).all()
    if cart_items:
        title = "Оплата заказа"
        description = "Оплата товаров из вашей корзины"
        payload = "Custom-Payload"
        currency = "RUB"
        prices = [LabeledPrice(f"{item.item.name} ({item.quantity} шт.)", int(item.item.price * 100 * item.quantity)) for item in cart_items]
    await context.bot.send_invoice(
        chat_id=update.message.chat_id,
        title=title,
        description=description,
        payload=payload,
        provider_token=PAYMENT_PROVIDER_TOKEN,
        currency=currency,
        prices=prices,
        start_parameter=&quot;test-payment&quot;,
        )
    else:
    await update.message.reply_text(quot;Ваша корзина пуста.&quot;)


async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.pre_checkout_query
    if query.invoice_payload != "Custom-Payload":
        await query.answer(ok=False, error_message="Что-то пошло не так...")
    else:
        await query.answer(ok=True)

async def successful_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session.query(CartItem).filter_by(user_id=update.message.chat_id).delete()
    session.commit()
    await update.message.reply_text("Спасибо за покупку! Ваш заказ был успешно оформлен.")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
app.add_handler(CommandHandler(&quot;start&quot;, start))
app.add_handler(CommandHandler(&quot;help&quot;, help_command))
app.add_handler(CommandHandler(&quot;catalog&quot;, catalog))
app.add_handler(CommandHandler(&quot;cart&quot;, view_cart))
app.add_handler(CommandHandler(&quot;checkout&quot;, checkout))
app.add_handler(MessageHandler(filters.TEXT &amp; ~filters.COMMAND, add_to_cart))
app.add_handler(PreCheckoutQueryHandler(precheckout_callback))
app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))

app.run_polling()

if __name__ == '__main__':
    if not session.query(Item).first():
        session.add_all([
            Item(name="Сервер", price=100.0),
            Item(name="Облако", price=150.0),
            Item(name="Amvera", price=200.0)
        ])
        session.commit()
main()

    
      
