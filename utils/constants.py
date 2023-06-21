SQLALCHEMY_BLOCK_NAME = 'sqlalchemy-connector-block'
TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS `stock_news` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `guidislink` tinyint(1) NOT NULL,
    `link` varchar(500) DEFAULT NULL,
    `published` timestamp NULL DEFAULT NULL,
    `stock_id` varchar(100) DEFAULT NULL,
    `summary` longtext,
    `title` varchar(500) DEFAULT NULL,
    `summary_details` longtext,
    PRIMARY KEY (`id`),
    UNIQUE KEY `UK_table_published_stock_id` (`published`,`stock_id`),
    KEY `stock_scheduler_stoc_stock_id_9ff65de8_fk_stock_sch` (`stock_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7759 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""
INSERT_QUERY = """
INSERT INTO `stock_news` (
    `guidislink`, `link`, `published`,
    `stock_id`, `summary`, `title`, `summary_details`
)
VALUES (
    :guidislink, :link, :published,
    :stock_id, :summary, :title, :summary_details
) ON DUPLICATE KEY
UPDATE
    guidislink = VALUES(guidislink),
    link = VALUES(link),
    summary = VALUES(summary),
    title = VALUES(title),
    summary_details = VALUES(summary_details);
"""