import tensorflow as tf


with tf.compat.v1.Session() as sess:
    frase = tf.constant('Ola, mundo!')
    rodar = sess.run(frase)
print(rodar)